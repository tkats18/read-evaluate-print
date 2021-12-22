mypy --python-version=3.9 --ignore-missing-imports --strict *.py
flake8 --max-line-length=88 --select=C,E,F,W,B,B950 --ignore=E501,W503 *.py
black *.py
isort --profile=black *.py