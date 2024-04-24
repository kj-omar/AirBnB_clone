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
    '''if  exists(archive_path):
        ext = os.path.splitext(archive_path)[-1]
        noext = ext.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, '/tmp/')
        run("mkdir -p {}{}".format(path, noext))
        run("tar -xzf /tmp/{}.tgz -C {}".format(noext, path))
        run("rm /tmp/{}".format(ext))
        run("mv {}{}/web_static/* {}{}/".format(path, noext, path,noext))
        run("rm -rf {}{}/web_static/".format(path, noext))
        run("rm -rf /data/web_static/current")
        run("ln -s {}{} /data/web_static/current".format(path, noext))
        print("New version deployed!")
        return True
    return False'''

    if not os.path.exists(archive_path):
        return False

    try:
        put(archive_path, '/tmp/')
        archive_filename = os.path.basename(archive_path)
        archive_name_no_ext = archive_filename.split('.')[0]
        release_folder = '/data/web_static/releases/{}'.format(archive_name_no_ext)
        run('sudo mkdir -p {}'.format(release_folder))
        run('sudo tar -xzf /tmp/{} -C {}'.format(archive_filename, release_folder))
        run('sudo rm /tmp/{}'.format(archive_filename))
        current_link = '/data/web_static/current'
        run('sudo rm -f {}'.format(current_link))
        run('sudo ln -s {} {}'.format(release_folder, current_link))
        print('New version deployed!')
        return True
    except Exception as e:
        print(e)
        return False
