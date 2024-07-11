#!/usr/bin/python3
"""Fabric Script for code deployment"""

import re
from fabric.api import cd, env, put, run, sudo

env.hosts = ["ubuntu@35.153.93.227", "ubuntu@100.26.175.131"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Deploys web_static"""

    if not archive_path:
        return(False)
    try:
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
        # print(f"{e}")
        return (False)
