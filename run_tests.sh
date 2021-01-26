#!/bin/bash

PKG=myaml

PYTHONPATH=$PWD:$PYTHONPATH py.test ${PKG}/ tests/

rm -rf .pytest_cache