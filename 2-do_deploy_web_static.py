#!/usr/bin/python3
"""Distributes an archive to web servers using the do_deploy function."""
from fabric.contrib import files
from fabric.api import env, put, run
import os

# Define the host servers
env.hosts = ['18.209.152.50', '34.229.136.68']


def do_deploy(archive_path):
    """Deploy the archive to the web servers."""
    # Check if the archive exists
    if not os.path.exists(archive_path):
        return False

    # Define the destination path on the server
    data_path = '/data/web_static/releases/'
    tmp = archive_path.split('.')[0]
    name = tmp.split('/')[1]
    dest = data_path + name

    try:
        # Upload the archive to the /tmp directory on the server
        put(archive_path, '/tmp')

        # Create the necessary directories on the server
        run('mkdir -p {}'.format(dest))

        # Extract the archive to the destination directory
        run('tar -xzf /tmp/{}.tgz -C {}'.format(name, dest))

        # Remove the uploaded archive from the server
        run('rm -f /tmp/{}.tgz'.format(name))

        # Move the contents of the extracted archive to the destination directory
        run('mv {}/web_static/* {}/'.format(dest, dest))

        # Remove the web_static directory from the destination directory
        run('rm -rf {}/web_static'.format(dest))

        # Remove the current symlink if it exists
        run('rm -rf /data/web_static/current')

        # Create a new symlink to the deployed version
        run('ln -s {} /data/web_static/current'.format(dest))

        return True
    except Exception:
        return False

