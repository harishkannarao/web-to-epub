init:
	pipenv install --dev

flake8:
	pipenv run flake8 --ignore=E501 --exclude=.venv,.git # ignore max line length

requirements:
	pipenv lock -r > requirements.txt
