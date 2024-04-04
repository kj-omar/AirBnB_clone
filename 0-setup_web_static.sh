#!/usr/bin/env bash
# Sets up a web server for deployment of web_static.

sudo apt-get update
if ! command -v nginx &> /dev/null; then
	sudo apt-get install -y nginx
fi

# create necessary directories
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/

# the fake file
echo "<html><head></head><body>Hoberton School</body></html>" | sudo tee /data/web_static/releases/test/index.html > /dev/null

# use -sf to fprcefully create or overwrite if currently present
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
# Give ownership of the /data/ folder to the ubuntu user and group recursively
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration to serve /data/web_static/current/ to hbnb_static using alias
sudo sed -i '/server_name _;/a \\n\tlocation /hbnb_static/
		{\n\t\talias /data/web_static/current/;\n\t}'
			/etc/nginx/sites-available/default

#restart nginx to apply chaanges
sudo service nginx restart

exit 0
