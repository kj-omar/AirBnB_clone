#!/usr/bin/python3
""" Fabric script that  creates and distributes an archive
to your web servers
"""
import os
from fabric.api import local, env, put, sudo
import datetime

env.hosts = ['100.26.152.53', '35.174.208.133']


def do_pack():
    """ function to create  .tgz archive """

    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.exists('./versions'):
        os.mkdir('./versions')
    archive_name = "web_static_" + time_stamp
    res = local("tar -czf versions/{}.tgz web_static".format(archive_name))
    print("Packing web_static to versions/{}.tgz".format(archive_name))
    if res.succeeded:
        size = os.path.getsize("versions/{}.tgz".format(archive_name))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
               archive_name, size))
        return archive_name + ".tgz"
    else:
        return None


def do_deploy(archive_path):
    """ function to deploy archive """
    if archive_path:
        a_name = os.path.basename(archive_path)
        a_folder_name = a_name.split('.')[0]
        path = "/data/web_static/releases/"

        put(archive_path, "/tmp")
        # Uncompress the archive
        sudo("mkdir -p /data/web_static/releases/{}".format(a_folder_name))
        sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}".format(
              a_name, a_folder_name))
        sudo("rm /tmp/{}".format(a_name))
        sudo("mv {0}{1}/web_static/* {0}{1}".format(path, a_folder_name))
        sudo("rm -rf /data/web_static/releases/{}/web_static".format(
              a_folder_name))
        sudo("rm /data/web_static/current")

        sudo("ln -s {0}{1}/ /data/web_static/current".format(
              path, a_folder_name))
        return True
    else:
        return False


def deploy():
    """ function handle full deployment """

    ar_path = do_pack()
    if ar_path is not None:
        res = do_deploy("versions/{}".format(ar_path))
        return res
    return False
