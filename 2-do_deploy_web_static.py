#!/usr/bin/python3
'''Fabric script that generates a .tgz archive'''
from fabric.api import local, put, run, env
from datetime import datetime
import os


def do_pack():
    '''unctin abric that generates a .tgz archive'''
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    tarre = "tar cvzf versions/web_static_{}.tgz web_static".format(time)

    local("mkdir -p versions")

    res = local(tarre)
    if res.failed:
        return None
    return f"versions/web_static_{time}.tgz"

def do_deploy(archive_path):
    '''distributes an archive to your web servers'''
    if not os.path.exists(archive_path):
        return False
    try:
        ext = os.path.splitext(archive_path)[-1]
        noext = ext.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run(f"mkdir -p {path}{noext}")
        run(f"tar -xzf /tmp/{noext}.tgz -C {path}")
        run(f"mv {path}{noext}/web_static/* {path}{noext}/")
        run(f"rm -rf {path}{noext}/web_static/")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {path}{noext} /data/web_static/current")
        print("New version deployed!")
        return True
    except:
        return False
