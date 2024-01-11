#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static

sudo apt-get -y update
sudo apt-get -y install nginx
mkdir /data/web_static/releases/test/ -p
mkdir /data/web_static/shared/ -p
echo "Holberton School" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -Rh ubuntu:ubuntu /data/
sed -i 's#server_name _;#server_name _;\n\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}#g' /etc/nginx/site_enabled/default
service nginx restart
