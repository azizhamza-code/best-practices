install:
		pip install --upgrade pip &&\
			pip install -r requirements.txt

format:

	black *.py 


lint:
	pylint --disable=R,C script.py

test:
	python -m pytest -vv --cov=script script_test.py