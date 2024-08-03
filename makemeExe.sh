#!/bin/bash
file=$1
echo "File Name: $file"
chmod u+x "$file"
echo "File Permissions: $(ls -l "$file" | cut -d ' ' -f 1)"
echo "File Type: $(file "$file" | cut -d ' ' -f 2-)"
