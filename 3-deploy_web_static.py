#!/usr/bin/python3
"""Fabric Script for code deployment"""

import re
from fabric.api import cd, env, put, run, sudo
from os import path

env.hosts = ["35.153.93.227", "100.26.175.131"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"
d_name = None

def deploy():
    """Creates and deploys to servers"""
    do_pack()
    if (d_name)
    do_deploy(d_name)


def do_pack():
    """Creates a .tgz file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"web_static_{time}.tgz"
    d_name = f"versions/{name}"
    local("mkdir -p ./versions")
    local(f"tar -czvf ./versions/{name} ./web_static")

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

        return (True)
    except Exception as e:
        print(f"{e}")
        return (False)
