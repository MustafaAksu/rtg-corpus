#!/usr/bin/env python3
"""Receive one hash-pinned ZIP. No archived code is executed; main is never written."""
import base64
import hashlib
import io
import json
import os
import urllib.error
import urllib.request
import zipfile

REPO = 'MustafaAksu/rtg-corpus'
BASE = '4e6bac05c2559716af8dde8d6cefafb6447447dd'
BASE_TREE = '3c6f7495b2e6028ebd8f63a4716a5fe8f4d766ca'
BRANCH = 'upload/dyad-cpp-centered-20261116'
ARCHIVE = 'DYAD_OPEN20_CPP_CENTERED_REVIEW_PACKAGE.zip'
DEST = 'evidence/dyad/open20-an/cpp-independent-intake/centered-20261116/'
EXPECTED = '5dfb8b1fd4b6decd3922c67611a57fa3330d31918f0f2f5f614d70c5223b068a'
EXPECTED_BLOB = '64d418a2bced65aaa14a825e7c6ca04627e2307b'
BLOBS = [
    'c297daedea336acb581a56de847d12e2de023b73',
    'a2844dcafb86077dd9b4778f4f95fcc325e2b3c6',
    'a1697349f21e440701e411160b7ae207d28e5924',
    '045825b26c70bbb324a82f8bce17e9637599edf9',
    '61fc874eada20189e0f262f4e986996bde3842b6',
    '1a3a9cc0896ff3fd8bca04e6cead0053204d30c6',
    '724626d1ba489172be63162890899be7e87fcefb',
    '07dd990798c4d39a8294382ecd763491566498de',
    'f45814fab777255e784ec516a95eb71403db3d37',
    'dc892047f5d5c5aa35346ba2db45eece92437a29',
    '7908eb3dd1597af6f6b7e8cd03e41052023b629b',
    '28bae18a70da60707c2bd922fb0d893c60c72f04',
    '4224e6d211389cc43396c4228e65cba6017dc900',
    'd44ce51802abed393b766160041045d4086d66b4',
    'c3e4ec3127c9c72e9780275b3af1a55a67302aaf',
    '785707d22b474ae383f3e7f2c7cd926f109c1f1b',
    '1f3431149e0a586599b2ce9d7924c5fda7218df4',
    '80e652e540d205c457e11b80437ed66c8bf035c4',
    '1e6c80c58de47147a9faf3d3c9b0d32fba803306',
]


def git_hash(data):
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def api(path, payload=None):
    req = urllib.request.Request(
        'https://api.github.com/repos/' + REPO + '/' + path,
        data=None if payload is None else json.dumps(payload).encode(),
        method='GET' if payload is None else 'POST',
        headers={
            'Authorization': 'Bearer ' + os.environ['GH_TOKEN'],
            'Accept': 'application/vnd.github+json',
            'Content-Type': 'application/json',
            'X-GitHub-Api-Version': '2022-11-28',
        },
    )
    with urllib.request.urlopen(req, timeout=45) as response:
        return json.load(response)


# Existing receipt branches are never overwritten.
try:
    api('git/ref/heads/' + BRANCH)
except urllib.error.HTTPError as exc:
    if exc.code != 404:
        raise
else:
    raise RuntimeError('Receipt branch already exists; no overwrite permitted')

chunks = []
for i, sha in enumerate(BLOBS):
    result = api('git/blobs/' + sha)
    assert result['encoding'] == 'base64'
    data = base64.b64decode(result['content'])
    assert result['sha'] == sha and git_hash(data) == sha
    if i == 2:
        # Two base64 characters were dropped in transport. Restore them, then
        # verify the original fragment hash and the complete original ZIP hash.
        text = base64.b64encode(data).decode()
        data = base64.b64decode(text[:5420] + '9P' + text[5420:] + 'w=', validate=True)
        assert git_hash(data) == '501940d3cce4f0161d569aaa66eb3a647eeb7a23'
        assert hashlib.sha256(data).hexdigest() == '4d9fb1a2ebe3fc4402ff46bb1457d86a2c7f0e2198b5b565162eec6d083dd468'
    assert len(data) == (8192 if i < 7 else (48 if i == 18 else 1024))
    chunks.append(data)
    print('Transport fragment', i, 'verified', flush=True)

data = b''.join(chunks)
assert len(data) == 68656
assert hashlib.sha256(data).hexdigest() == EXPECTED
assert git_hash(data) == EXPECTED_BLOB
with zipfile.ZipFile(io.BytesIO(data)) as archive:
    names = archive.namelist()
    assert len(names) == len(set(names)) == 35
    assert archive.testzip() is None
    manifest = {}
    for line in archive.read('SHA256SUMS.txt').decode().splitlines():
        digest, name = line.split('  ', 1)
        assert name not in manifest
        manifest[name] = digest
    assert len(manifest) == 34
    assert set(manifest) == set(names) - {'SHA256SUMS.txt'}
    for name, digest in manifest.items():
        assert hashlib.sha256(archive.read(name)).hexdigest() == digest
print('Original ZIP verified: 68656 bytes; SHA256', EXPECTED, '; 34/34 internal hashes', flush=True)

# Publish only the original archive and checksum, from the pinned base tree.
base = api('git/commits/' + BASE)
assert base['tree']['sha'] == BASE_TREE
blob = api('git/blobs', {'encoding': 'base64', 'content': base64.b64encode(data).decode()})
assert blob['sha'] == EXPECTED_BLOB
checksum = EXPECTED + '  ' + ARCHIVE + '\n'
tree = api('git/trees', {'base_tree': BASE_TREE, 'tree': [
    {'path': DEST + ARCHIVE, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']},
    {'path': DEST + 'SHA256SUMS.txt', 'mode': '100644', 'type': 'blob', 'content': checksum},
]})
commit = api('git/commits', {
    'message': 'upload/dyad: receive unchanged Boost centred C++ review package\n\n'
               'PI-requested intake only. Original ZIP SHA256 ' + EXPECTED + '.\n'
               '35 members, 34 internal hashes verified. No source execution, placement, adoption or certification.\n'
               'MPFR draft PR #287 is parked; owner review PR #288 governs receiving scope.',
    'tree': tree['sha'], 'parents': [BASE],
})
ref = api('git/refs', {'ref': 'refs/heads/' + BRANCH, 'sha': commit['sha']})
assert ref['object']['sha'] == commit['sha']
print('RECEIVED', BRANCH, commit['sha'], flush=True)
with open(os.environ['GITHUB_STEP_SUMMARY'], 'a') as summary:
    summary.write('## Unchanged archive received\n\nCommit: `' + commit['sha'] + '`\n\n'
                  'Branch: `' + BRANCH + '`\n\nSHA256: `' + EXPECTED + '`\n\n'
                  '35 ZIP members; 34/34 internal hashes. No mathematical code executed.\n')
