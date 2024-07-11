#!/usr/bin/python3
"""Fabric Script for code deployment"""

from fabric.api import cd, env, put, run, sudo

env.hosts = ["ubuntu@35.153.93.227", "ubuntu@100.26.175.131"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Deploys web_static"""

    try:
        if archive_path is None:
            return(False)
        # Upload file
        put(archive_path, '/tmp/')

        # Find filename and directory name from archive_path
        pattern = r'([^/]+)\.tgz$'
        directory = re.search(pattern, archive_path).group(1)
        filename = f"{directory}.tgz"

        # Decompressing archive
        run(f"mkdir -p /data/web_static/releases/{directory}/")
        run(f"tar -xzf /tmp/{filename} -C "
            f"/data/web_static/releases/{directory}/")

        # Deleting archive
        run(f"rm /tmp/{filename}")

        # Deploying new version
        run(f"mv /data/web_static/releases/{directory}/web_static/* "
            f"/data/web_static/releases/{directory}/")
        run(f"rm -rf /data/web_static/releases/{directory}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s /data/web_static/releases/{directory}/ "
            "/data/web_static/current")
    except:
        return (False)
    return (True)
