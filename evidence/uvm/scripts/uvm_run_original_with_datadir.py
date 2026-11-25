"""
uvm_run_original_with_datadir.py -- [SESSION] runner for open_m_2f_trajectory.py

Executes an original certificate script unchanged except for ONE textual
substitution: its hard-coded input directory "/mnt/user-data/uploads/" is
replaced by the directory given on the command line. The substitution must
occur exactly once, or the runner stops. The script's SHA-256 and the
substitution count are printed to stderr.

Usage:
  python3 -I uvm_run_original_with_datadir.py <original_script.py> <data_dir>
"""
import sys, hashlib
src_path, data_dir = sys.argv[1], sys.argv[2].rstrip('/\\') + '/'
src = open(src_path, encoding='utf-8').read()
n = src.count('/mnt/user-data/uploads/')
print(f"[runner] script sha256 {hashlib.sha256(src.encode('utf-8')).hexdigest()}; substitution count {n}", file=sys.stderr)
if n != 1:
    sys.exit("[runner] expected exactly one occurrence of /mnt/user-data/uploads/")
sys.argv = [src_path]
exec(compile(src.replace('/mnt/user-data/uploads/', data_dir), src_path, 'exec'), {'__name__': '__main__'})
