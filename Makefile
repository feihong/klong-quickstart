upgrade:
	pip install --upgrade klongpy

py:
	rlwrap kgpy

kg:
	rlwrap --always-readline kg

cheatsheet:
	python generate-cheatsheet.py
