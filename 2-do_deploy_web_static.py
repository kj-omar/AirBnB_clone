#!/usr/bin/python3
"""Comment wihtout any fuckin reason"""
from datetime import datetime
from fabric.api import *
from os.path import exists, basename, splitext
env.use_ssh_config = True
env.hosts = ["54.87.203.83", "54.144.147.110"]
"""Importing the libraries in the file of the functions"""


@task
def do_deploy(archive_path):
    """Function to deploy the web servers"""
    if not exists(archive_path):
            return False
    try:
        ext = basename(archive_path)
        no_ext, ext = splitext(ext)
        web_server_ext = "/data/web_static/releases/"
        # List of commands to be executed in the hosts side
        commands = [f"rm -rf {web_server_ext}{no_ext}/",
                    f"mkdir -p {web_server_ext}{no_ext}/",
                    f"tar -xzf /tmp/{no_ext}{ext} -C {web_server_ext}{no_ext}/",
                    f"rm /tmp/{no_ext}{ext}",
                    f"mv {web_server_ext}{no_ext}/web_static/* {web_server_ext}{no_ext}/",
                    f"rm -rf {web_server_ext}{no_ext}/web_static",
                    f"rm -rf /data/web_static/current",
                    f"ln -s {web_server_ext}{no_ext}/ /data/web_static/current"]
        for command in commands:
            run(command)
        print("New version deployed!")
        return True
    except Exception as e:
        return False


@task
def do_pack():
    """
    This function can do hard things
    """
    # Create the versions directory if it doesn't exist
    mkdir = "mkdir -p versions"
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    # Define the name of the archive
    archive_name = f"web_static_{timestamp}.tgz"
    archive_path = f"versions/{archive_name}"

    # Create the archive
    command = f"{mkdir} && tar -cvzf {archive_path} web_static"
    result = local(command)

    # Check if the archive was created successfully
    if result.succeeded:
        return archive_path
    else:
        return None
