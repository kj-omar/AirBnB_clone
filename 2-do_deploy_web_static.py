#!/usr/bin/python3
"""Script to compress the web static package
"""
from fabric.api import *
from datetime import datetime
from os import path

# Define the hosts, user, and key for connecting to the servers
env.hosts = ['100.25.19.204', '54.157.159.85']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Deploy web files to the server
    """
    try:
        if not path.exists(archive_path):
            return False

        # Upload the archive to the server
        put(archive_path, '/tmp/')

        # Create the target directory
        timestamp = archive_path[-18:-4]
        run('sudo mkdir -p /data/web_static/releases/web_static_{}/'.format(timestamp))

        # Uncompress the archive and delete the .tgz file
        run('sudo tar -xzf /tmp/web_static_{}.tgz -C /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # Remove the archive from the server
        run('sudo rm /tmp/web_static_{}.tgz'.format(timestamp))

        # Move the contents to the web_static directory on the server
        run('sudo mv /data/web_static/releases/web_static_{}/web_static/* /data/web_static/releases/web_static_{}/'.format(timestamp, timestamp))

        # Remove the extra web_static directory
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.format(timestamp))

        # Delete the existing symbolic link
        run('sudo rm -rf /data/web_static/current')

        # Create a new symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{}/ /data/web_static/current'.format(timestamp))
    except:
        return False

    # Return True if the deployment is successful
    return True
