#!/bin/bash
# run unit tests

tests=("test_base_model.py"  "test_amenity.py" "test_city.py" "test_place.py" "test_user.py" "test_review.py" "test_state.py")

for test in "${tests[@]}";
do
    echo "Running unittests for $test..."
    python3 -m unittest tests/test_models/"$test"
done



echo "done"