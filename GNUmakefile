default: egg

PYTHON=$(shell which python)
HERE:=$(PWD)

egg:
    # setup.py will call 'make build' before creating the egg
	python setup.py bdist_egg

build:
	echo "Nothing to build"

clean:
	rm -rf lib build dist
	rm -rf ZenPacks.zenoss.MSSQLServer.egg-info
