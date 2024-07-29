#!/usr/bin/python3
"""Comment wihtout any fuckin reason"""
from datetime import datetime
from fabric.api import *
"""Importing the libraries in the file of the functions"""

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
