#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['100.25.19.204', '54.157.159.85']

def do_pack():
    """Create a tar gzipped archive of the web_static directory."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed:
        return None
    return file

def do_deploy(archive_path):
    """Deploy an archive to the web server.

    Args:
        archive_path (str): Path to the archive file to deploy.
    Returns:
        bool: False if the file doesn't exist or an error occurs, True otherwise.
    """
    if not os.path.isfile(archive_path):
        return False
    file = os.path.basename(archive_path)
    name = file.split(".")[0]

    if put(archive_path, "/tmp/{}".format(file)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed:
        return False
    if run("rm /tmp/{}".format(file)).failed:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed:
        return False
    if run("rm -rf /data/web_static/current").failed:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed:
        return False
    return True

def deploy():
    """Create and deploy an archive to the web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
