.PHONY: reproduce validate figures evidence checksums extract
reproduce:
	python run_all.py
validate:
	python scripts/00_validate_inputs.py
figures:
	python scripts/01_generate_results.py
	python scripts/02_make_figures.py
evidence:
	python scripts/03_audit_manual_evidence.py
checksums:
	python scripts/05_verify_checksums.py
extract:
	python scripts/04_extract_cpp.py
