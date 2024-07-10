#!/usr/bin/python3
""" pack, and deploy to server """
from fabric.api import *
from datetime import datetime
from os.path import exists, isdir

env.hosts = ['54.237.5.6', '100.26.221.163']


def do_pack():
    """ generates .tgz achive """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception as e:
        return None


def do_deploy(archive_file):
    """ deploy to server """
    if not exists(archive_file):
        return False
    try:
        put(archive_file, "/tmp/")
        file = archive_file.split("/")[-1]
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


def deploy():
    """ pack and deploy """
    archive = do_pack()
    if archive is None:
        return False
    return do_deploy(archive)
