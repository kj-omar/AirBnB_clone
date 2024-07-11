#!/usr/bin/env bash
# Set up web servers for the deployment of web_static

if ! command -v nginx > /dev/null 2>&1; then
    sudo apt-get update
    sudo apt-get install -y nginx
fi

sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
echo "hello fab!" > /data/web_static/releases/test/index.html

Target="/data/web_static/releases/test/"
Sym_link="/data/web_static/current"

if [ -L "$Sym_link" ]; then
    sudo rm "$Sym_link"
fi

sudo ln -s "$Target" "$Sym_link"

sudo chown -R ubuntu:ubuntu /data

sudo sed -i "51i\ \tlocation /hbnb_static{\n \
\t\talias /data/web_static/current/;\n\
\t}" /etc/nginx/sites-enabled/default

sudo service nginx restart
