rm -rf dist
python3 setup.py sdist bdist_wheel
/Users/joubin/Library/Python/3.7/bin/twine upload  dist/*
#/Users/joubin/Library/Python/3.7/bin/twine upload --repository-url https://test.pypi.org/legacy/ dist/*
