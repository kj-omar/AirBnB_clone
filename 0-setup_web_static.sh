#!/usr/bin/env bash
# Script sets up web server for deployment of web_static.

sudo apt-get update
sudo apt-get install nginx
sudo ufw allow 'Nginx HTTP'

# make directories
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/

# make a fake HTML file
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html><head></head><body>Hello World!</body></html>" > /data/web_static/releases/test/index.html

# make a symbolic link, if exist delete and recreate everytime script is run
link_path="/data/web_static/current"
target="/data/web_static/releases/test/"

# check if the symbolic link already exists
if [ -L "$link_path" ]; then
	rm "$link_path"
fi

# recreate new symbolic link
sudo ln -s "$target" "$link_path"

# change owner and group to ubuntu user recursively
sudo chown -R ubuntu:ubuntu /data/

# update the Nginx configuration
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# restart Nginx
sudo service nginx restart
