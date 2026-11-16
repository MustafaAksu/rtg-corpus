#!/usr/bin/env python3
"""Verify the received DZT payload; optionally extract without executing originals."""
import argparse
import hashlib
import io
import json
import sys
import tarfile
from pathlib import Path, PurePosixPath


def require(condition, message):
    if not condition:
        raise ValueError(message)


def sha(data):
    return hashlib.sha256(data).hexdigest()


def safe_path(name):
    p = PurePosixPath(name)
    require(bool(name) and not p.is_absolute() and '..' not in p.parts
            and '\\' not in name and ':' not in name and str(p) == name,
            'Unsafe or noncanonical path: ' + name)
    return p


def verify(root):
    m = json.loads((root / 'TRANSPORT_MANIFEST.json').read_text(encoding='utf-8'))
    require(m['schema'] == 'dzt-lossless-transport-v1', 'Unknown schema')
    parts = []
    names = set()
    for part in m['parts']:
        name = part['name']
        require(len(safe_path(name).parts) == 1 and name not in names,
                'Invalid or repeated part name')
        names.add(name)
        data = (root / 'payload' / name).read_bytes()
        require(len(data) == part['size'] and sha(data) == part['sha256'],
                'Part integrity failure: ' + name)
        parts.append(data)
    archive = b''.join(parts)
    require(len(archive) == m['archive']['bytes']
            and sha(archive) == m['archive']['sha256'], 'Archive integrity failure')
    files = {}
    with tarfile.open(fileobj=io.BytesIO(archive), mode='r:xz') as t:
        members = t.getmembers()
        require(len(members) == m['archive']['entries'] == 71, 'Entry count mismatch')
        require(sum(x.size for x in members) == m['archive']['entry_bytes'] == 1776029,
                'Entry byte count mismatch')
        for member in members:
            safe_path(member.name)
            require(member.isfile() and member.name not in files,
                    'Nonregular or duplicate archive entry')
            require(0 <= member.size <= 2000000, 'Oversized entry')
            stream = t.extractfile(member)
            require(stream is not None, 'Unreadable member')
            files[member.name] = stream.read()
    for name, digest in m['package_file_sha256'].items():
        require(name in files and sha(files[name]) == digest,
                'Collection metadata mismatch: ' + name)
    manifest = json.loads(files['MANIFEST.json'].decode('utf-8-sig'))
    require(manifest['schema'] == 'dzt-intake-local-v1', 'Unknown collection schema')
    rows = manifest['files']
    paths = [r['package_path'] for r in rows]
    require(len(rows) == len(set(paths)) == m['originals']['files'] == 67,
            'Original file count mismatch')
    require(set(files) == set(paths) | set(m['package_file_sha256']),
            'Unlisted or missing payload')
    hashes = set()
    total = 0
    for row in rows:
        name = row['package_path']
        require(safe_path(name).parts[0] == 'originals', 'Invalid original location')
        data = files[name]
        digest = sha(data)
        require(len(data) == row['bytes'] and digest == row['sha256'].lower(),
                'Original integrity failure: ' + name)
        total += len(data)
        hashes.add(digest)
    require(total == m['originals']['bytes'] == 1725716, 'Original byte count mismatch')
    require(len(hashes) == m['originals']['unique_hashes'] == 54, 'Unique count mismatch')
    sums = {}
    for line in files['SHA256SUMS'].decode('utf-8-sig').splitlines():
        digest, name = line.split('  ', 1)
        require(name not in sums, 'Duplicate SHA256SUMS entry')
        sums[name] = digest.lower()
    require(sums == {r['package_path']: r['sha256'].lower() for r in rows},
            'SHA256SUMS and original manifest disagree')
    return files


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--extract', action='store_true',
                        help='Write validated files to a new received/ directory')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    files = verify(root)
    if args.extract:
        destination = root / 'received'
        destination.mkdir(exist_ok=False)
        for name, data in files.items():
            target = destination.joinpath(*safe_path(name).parts)
            target.parent.mkdir(parents=True, exist_ok=True)
            with target.open('xb') as output:
                output.write(data)
            require(sha(target.read_bytes()) == sha(data), 'Written file mismatch: ' + name)
        print('EXTRACTED_TO=' + str(destination))
    print('TRANSPORT_VERIFICATION=PASS')
    print('SOURCE_FILES=67\nSOURCE_BYTES=1725716\nUNIQUE_CONTENT_HASHES=54')
    print('ORIGINAL_FILES_EXECUTED=0\nGIT_ACTIONS=0')
    return 0


if __name__ == '__main__':
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError, TypeError, tarfile.TarError, EOFError) as exc:
        print('INTAKE_VERIFICATION=FAIL: ' + str(exc), file=sys.stderr)
        sys.exit(1)
