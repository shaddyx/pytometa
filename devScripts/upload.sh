#!/bin/bash

pushd ../src
rm -rf dist
python setup.py sdist
#twine register dist/* -r pypi
twine upload dist/*
rm -rf dist
popd