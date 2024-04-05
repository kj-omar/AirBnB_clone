#!/usr/bin/env bash
# Bash script to set up web servers for the deployment of web_static

# Update package lists and install Nginx
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary directories for storing web static files
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo touch /data/web_static/releases/test/index.html


# Create a test HTML file with content
sudo echo "<html>
	<head>
	</head>
	<body>
	Holberton School
	</body>
	</html>" |sudo tee  /data/web_static/releases/test/index.html

# Set up a symbolic link to point current to the test release
sudo ln -s -f /data/web_static/releases/test/ /data/web_static/current

# Change ownership of directories to user ubuntu
sudo chown -R ubuntu:ubuntu /data/

# Configure Nginx to serve static content
# Add an alias for serving /hbnb_static from the current folder
sudo sed -i '/listen 80 default_server/a location /hbnb_static { alias /data/web_static/current/;}' /etc/nginx/sites-enabled/default

# Restart Nginx to apply the changes
sudo service nginx restart

