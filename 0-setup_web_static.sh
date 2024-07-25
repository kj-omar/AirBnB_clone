#!/usr/bin/env bash
# making the deploying bash file

# ensuring that the nginx is installed on the server
trap 'exit 0' ERR
if ! command -v nginx &> /dev/null; then
    apt-get update -y
    apt-get install nginx -y
fi

# making the folders and setting up the environment
mkdir -p /data/web_static/shared/
mkdir -p /data/web_static/releases/test/

dat=$(date +"%Y-%m-%d %H-%M-%S")
content="<head>
<title> My_web </title>
</head>
<body>
    <h1>Hellow there this is a new brand web here</h1>
    <p>Date created: $dat</p>
</body>"

echo "$content" > /data/web_static/releases/test/index.html

rm -rf /data/web_static/current
ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu:ubuntu /data/
vr=$(hostname)
conf="/etc/nginx/sites-available/default"
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root /etc/nginx/html;
    add_header X-Served-By $vr;
    rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html;
    }
    error_page 404 /40x.html;
    location = /40x.html {
        root /etc/nginx/error_files;
        internal;
      }
    index index.html;
}" > $conf

service nginx restart
