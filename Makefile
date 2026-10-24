.PHONY: pdf verifier release
pdf:
	python3 compiler.py $(if $(NIVEAU),--niveau $(NIVEAU),)
verifier:
	python3 -m unittest discover -s scripts -p 'test_*.py'
	python3 compiler.py
	python3 scripts/verifier_collection.py
release: verifier
	python3 scripts/preparer_release.py
