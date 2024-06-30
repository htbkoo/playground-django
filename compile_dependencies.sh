#!/bin/bash

# TODO: add setup to confirm `pyenv` is configured + installation of `pip` and `pip-tools`

CUSTOM_COMPILE_COMMAND="./compile_dependencies.sh" pip-compile --output-file requirements.txt requirements.in
CUSTOM_COMPILE_COMMAND="./compile_dependencies.sh" pip-compile --output-file test_requirements.txt test_requirements.in
