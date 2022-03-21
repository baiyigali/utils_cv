# remove build and dist folder first
rm build dist -rf
python3 setup.py test
# python3 -m unittest discover
python3 setup.py sdist bdist_wheel
python3 -m twine upload dist/*
