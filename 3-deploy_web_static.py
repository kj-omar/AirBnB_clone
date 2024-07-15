#!/usr/bin/python3
""" Fabric script that  creates and distributes an archive
to  web servers
"""
import os
from fabric.api import local, env, put, sudo, runs_once, run
import datetime

hosts = ['100.26.152.53', '35.174.208.133']


@runs_once
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
        full_path = "versions/{}.tgz".format(archive_name)
        return full_path
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


def deploy():
    """ function handle full deployment """
    path = do_pack()
    if path is not None:
        for host in hosts:
            env.host_string = host
            result = do_deploy(path)
        return result
    return False
