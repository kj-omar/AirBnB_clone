#!/usr/bin/python3
""" Fabric script that distributes an archive to your web servers,"""
from fabric.api import *
from os.path import exists

env.hosts = ['54.237.5.6', '100.26.221.163']


def do_deploy(archive_path):
    """ deploy to server """
    if not exists(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")
        file = archive_path.split("/")[-1]
        folder = "/data/web_static/releases/" + file.split(".")[0]
        run("mkdir -p {}".format(folder))
        run("tar -xzf /tmp/{} -C {}".format(file, folder))
        run("rm /tmp/{}".format(file))
        run("mv {}/web_static/* {}/".format(folder, folder))
        run("rm -rf {}/web_static".format(folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(folder))
        return True
    except Exception:
        return False
