#!/usr/bin/env bash
# Bash script that sets up your web servers for the deployment of web_static

#Update and install nginx
sudo apt update
sudo apt -y install nginx
sudo ufw allow 'Nginx HTTP'

#Create directories, symbolic links and files
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html
sudo echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test /data/web_static/current

sudo chown -R ubuntu:ubuntu /data/

#sed -i '/listen 80 default_server/a '"\
#"'\        location /hbnb_static {\n'"\
#"'                alias /data/web_static/current/;\n'"\
#"'        }' /etc/nginx/sites-enabled/default

printf %s "server {
        listen 80 default_server;
        listen [::]:80 default_server;

        server_name _;

        root /var/www/html;
        index index.html index.htm index.nginx-debian.html;

        add_header X-Served-By \$hostname;

        location / {
            try_files \$uri \$uri/ =404;
        }

        location /hbnb_static {
            alias /data/web_static/current/;
        }

        if (\$request_filename ~ redirect_me){
                rewrite ^ https://youtube.com permanent;
        }

        error_page 404 /404.html;
        location = /404.html {
            internal;
        }
}" | sudo tee /etc/nginx/sites-enabled/default

sudo service nginx restart
