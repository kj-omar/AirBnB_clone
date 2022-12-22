#!/usr/bin/python3
"""creates and distributes an archive to
your web servers, using the function deploy"""
from fabric.api import env, put, run
from os import path

# archive_path = 'versions/web_static_20221221225808.tgz'
archive_path = __import__("1-pack_web_static").do_pack()
env.host = ['52.91.116.127', '100.25.45.223']
env.user = 'ubuntu'


def deploy():
    try:
        if not path.exists(archive_path):
            raise Exception
        file_name_tgz = archive_path.split('/')[-1]
        file_name = file_name_tgz.split('.')[0]
        versions_path = "versions/{}".format(file_name_tgz)
        tmp_path = "/tmp/{}".format(file_name_tgz)
        release_path = "/data/web_static/releases/{}/".format(file_name)
        put(versions_path, '/tmp/')
        run("mkdir -p {}".format(release_path))
        run("tar -xzf {} -C {}".format(tmp_path, release_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(release_path))
        run("rm -rf {}web_static".format(release_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(release_path))
        print("New version deployed!")
        return archive_path
    except Exception:
        return False
