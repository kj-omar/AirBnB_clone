#!/usr/bin/python3
""" fabric script that distributes an archive to my
web servers, using do_deploy function"""

from fabric.api import put
from fabric.api import env
from fabric.api import run
from os import path

env.hosts = ['54.160.65.25', '3.90.80.134']


def do_deploy(archive_path):
    """function distributes an archive to my web server
    Args:
        archive_path: Path to be distributed as a string
        Returns: error - False
        otherwise - True
    """
    if path.isfile(archive_path) is False:
        return False
    folder = archive_path.split("/")[-1]
    peter = folder.split(".")[0]

    if put(archive_path, "/tmp/{}".format(folder)).failed is True:
        return False
    if run('rm -rf /data/web_static/releases/{}/'.
            format(peter)).failed is True:
        return False
    if run('mkdir -p /data/web_static/releases/{}/'.
            format(peter)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /datat/web_static/releases/{}/".
            format(folder, peter)).failed is True:
        return False
    if run("rm /tmp/{}".format(folder)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(peter, peter)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
            format(peter)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(peter)).failed is True:
        return False
    return True
