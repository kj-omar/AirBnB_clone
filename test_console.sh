#!/bin/bash

echo "Testing the console...."
cat test_params_create | HBNB_MYSQL_USER=hbnb_dev HBNB_MYSQL_PWD=hbnb_dev_pwd HBNB_MYSQL_HOST=localhost HBNB_MYSQL_DB=hbnb_dev_db HBNB_TYPE_STORAGE=db python ./console.py

if [ $? -eq 0 ]; then
	echo "test succeded"
else
	echo "test failed"
fi
