#!/usr/bin/env bash

apt-get update
apt-get install y ngix

mkdir -p /data/web_static/releases/test/index.html
mkdir -p /data/web_static/shared/
echo "HELLO WORLD" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/curl

chown -R ubuntu /data/
chgrp -R ubuntu /data/
configurations="
server{
    listen 80 default_server;
    listen [::]:80 default_server;

    server_name _;

    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

    error_page 404 /404.html;
        location /404 {
                root /var/www/html;
                internal;
    }

}"
echo "$configurations" > /etc/nginx/sites-available/default

service ngix restart
