#!/bin/bash

# Run the tests and print the last line of output
# (which will be the summary of the test results)

echo "Discovering..."

python3 -m unittest discover tests 2>&1 /dev/null | tail -n 1

sleep 2

echo "done"
