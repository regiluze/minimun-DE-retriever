#!/bin/bash

find . -name *.pyc -delete
echo
echo "----------------------------------------------------------------------"
echo "Running acceptance Specs"
echo "----------------------------------------------------------------------"
echo

TEST_PATH="specs"

if [[ -z "$1" ]]; then
    FORMATTER="progress"
elif [[ "$1" == "doc" ]]; then
    FORMATTER="documentation"
fi
echo $FORMATTER

mamba -f $FORMATTER acceptance_specs/*

MAMBA_RETCODE=$?

exit $MAMBA_RETCODE
