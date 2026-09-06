from pathlib import Path
import subprocess, sys

ROOT=Path(__file__).resolve().parent
SCRIPTS=[
    '00_validate_inputs.py',
    '01_generate_results.py',
    '03_audit_manual_evidence.py',
    '05_verify_checksums.py',
    '02_make_figures.py',
]
for script in SCRIPTS:
    print(f'\n== {script} ==')
    subprocess.run([sys.executable,str(ROOT/'scripts'/script)],check=True,cwd=ROOT)
print('\nReproduction complete.')
print('See data/derived/ for regenerated numerical summaries and figures/ for regenerated poster figures.')
print('Optional: python scripts/04_extract_cpp.py to extract fenced C++ blocks from the 120 raw responses.')
