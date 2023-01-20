
.PONY: py/packages py/codestyle py/format

py/packages:
	@pip install -r requirement.txt

py/codestyle: #checks PEP8
	@flake8 src

py/format: #format python code
	@black src