#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static
"""
import os
from fabric.api import run, env, put
import datetime

env.hosts = ['100.26.152.53', '35.174.208.133']

def do_deploy(archive_path):
    """ function to deploy archive """
    if archive_path:
        a_name = os.path.basename(archive_path)
        a_folder_name = f_name.split('.')[0]

        put(archive_path, "/tmp")
        # Uncompress the archive
        sudo("tar -xzf /tmp/a_name -C /data/web_static/releases/{}".format(a_folder_name))
        sudo(f'rm /tmp/{a_name}')
        sudo('rm /data/web_static/current')

        sudo(f'ln -s /data/web_static/releases/{a_folder_name} /data/web_static/current')
        return True
    else:
        return False
