# Puppet configuration for setting up NGINX server

# NGINX configuration
$nginx_conf = "server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By ${hostname};
    root   /var/www/html;
    index  index.html index.htm;
    location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }
    location /redirect_me {
        return 301 http://linktr.ee/firdaus_h_salim/;
    }
    error_page 404 /404.html;
    location /404 {
      root /var/www/html;
      internal;
    }
}"

# Ensure NGINX package is present
package { 'nginx':
  ensure   => 'present',
  provider => 'apt'
}

# Create necessary directories
-> file { '/data':
  ensure  => 'directory'
}

-> file { '/data/web_static':
  ensure => 'directory'
}

-> file { '/data/web_static/releases':
  ensure => 'directory'
}

-> file { '/data/web_static/releases/test':
  ensure => 'directory'
}

-> file { '/data/web_static/shared':
  ensure => 'directory'
}

# Create index.html in test directory
-> file { '/data/web_static/releases/test/index.html':
  ensure  => 'present',
  content => "this webpage is found in data/web_static/releases/test/index.htm \n"
}

# Create symbolic link to current directory
-> file { '/data/web_static/current':
  ensure => 'link',
  target => '/data/web_static/releases/test'
}

# Change ownership of /data directory
-> exec { 'chown -R ubuntu:ubuntu /data/':
  path => '/usr/bin/:/usr/local/bin/:/bin/'
}

# Create necessary directories for NGINX
file { '/var/www':
  ensure => 'directory'
}

-> file { '/var/www/html':
  ensure => 'directory'
}

# Create index.html and 404.html in NGINX root directory
-> file { '/var/www/html/index.html':
  ensure  => 'present',
  content => "This is my first upload  in /var/www/index.html***\n"
}

-> file { '/var/www/html/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page - Error page\n"
}

# Configure NGINX default site
-> file { '/etc/nginx/sites-available/default':
  ensure  => 'present',
  content => $nginx_conf
}

# Restart NGINX service
-> exec { 'nginx restart':
  path => '/etc/init.d/'
}

