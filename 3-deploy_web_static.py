#!/usr/bin/python3
"""Fabric Script for code deployment"""

import re
from datetime import datetime
from fabric.api import cd, env, put, local, run, sudo
from os import path

env.hosts = ["35.153.93.227", "100.26.175.131"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def deploy():
    """Creates and deploys to servers"""
    path_string = do_pack()
    if not (path.exists(path_string)):
        return (False)
    value = do_deploy(path_string)
    return (value)


def do_pack():
    """Creates a .tgz file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"web_static_{time}.tgz"
    zip_path = f"versions/{name}"
    local("mkdir -p ./versions")
    local(f"tar -czvf ./versions/{name} ./web_static")
    if not (path.exists(zip_path)):
        return (False)
    return (zip_path)


def do_deploy(archive_path):
    """Deploys web_static"""

    try:
        if not (path.exists(archive_path)):
            return (False)
        # Upload file
        put(archive_path, '/tmp/')

        # Find filename and directory name from archive_path
        pattern = r'([^/]+)\.tgz$'
        directory = re.search(pattern, archive_path).group(1)
        filename = f"{directory}.tgz"

        # Decompressing archive
        run(f"sudo mkdir -p /data/web_static/releases/{directory}/")
        run(f"sudo tar -xzf /tmp/{filename} -C "
            f"/data/web_static/releases/{directory}/")

        # Deleting archive
        run(f"sudo rm /tmp/{filename}")

        # Deploying new version
        run(f"sudo mv /data/web_static/releases/{directory}/web_static/* "
            f"/data/web_static/releases/{directory}/")
        run(f"sudo rm -rf /data/web_static/releases/{directory}/web_static")
        run("sudo rm -rf /data/web_static/current")
        run(f"sudo ln -s /data/web_static/releases/{directory}/ "
            "/data/web_static/current")
        print("New version deployed!")

        return (True)
    except Exception as e:
        print(f"{e}")
        return (False)
