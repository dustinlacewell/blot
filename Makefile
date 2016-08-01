doc:
	cd docs && ./build_docs


test:
	nosetests -s blot

coverage:
	nosetests --with-coverage --cover-package=blot --cover-html -s blot

release:
	python setup.py sdist upload
