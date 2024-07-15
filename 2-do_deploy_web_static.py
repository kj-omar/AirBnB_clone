#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
from the contents of the web_static
"""
import os
from fabric.api import env, run, put, sudo
import datetime

env.hosts = ['100.26.152.53', '35.174.208.133']


def do_deploy(archive_path):
    """ function to deploy archive """
    if archive_path:
        a_name = os.path.basename(archive_path)
        a_folder_name = a_name.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp")
        # Uncompress the archive
        run("mkdir -p /data/web_static/releases/{}".format(a_folder_name))
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
              a_name, a_folder_name))
        run("rm /tmp/{}".format(a_name))
        run("mv {0}{1}/web_static/* {0}{1}".format(path, a_folder_name))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
              a_folder_name))
        run("rm /data/web_static/current")

        run("ln -s {0}{1}/ /data/web_static/current".format(
              path, a_folder_name))
        return True
    else:
        return False
