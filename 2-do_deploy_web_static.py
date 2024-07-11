#!/usr/bin/python3
"""Fabric Script for code deployment"""

from fabric.api import cd, env, put, run, sudo

#env.hosts = ["ubuntu@35.153.93.227", "ubuntu@100.26.175.131"]
env.hosts = ["ubuntu@35.153.93.227"]
env.key_filename = "~/.ssh/id_rsa"


def do_deploy(archive_path):
    """Deploys web_static"""

    if archive_path is None:
        return(False)
    #Upload file
    put(archive_path, /tmp/)
        pattern = r'([^/]+)\.tgz$'

    #Find filename and directory name from archive_path
    directory = re.search(pattern, archive_path).group(1)
    filename = f"{directory}.tgz"

    #Decompressing archive
    run(f"mkdir -p /data/web_static/releases/{directory}")
    run(f"tar -xzf /tmp/{filename}, -C /data/web_static/releases/{directory}/")

    #Deleting archive
    run(f"rm /tmp/{filename}")


    run("rm -rf /data/web_static/current")
    run(f"ln -s /data/web_static/releases/{directory} /data/web_static/current")


def do_pack():
    """Creates a .tgz file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"web_static_{time}.tgz"
    local("mkdir -p ./versions")
    local(f"tar -czvf ./versions/{name} ./web_static")

