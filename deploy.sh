#!/bin/bash

clean () {
    rm -rf build dist *.egg-info
}

clean

python setup.py sdist bdist_wheel
sleep 1

twine check dist/* && twine upload --repository pypi dist/*

clean