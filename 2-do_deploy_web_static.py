#!/usr/bin/python3
"""
This Python module facilitates the deployment of archives to web servers.
"""

from os import path

from fabric.api import env, put, run

# Define the server environment
env.hosts = ["18.206.207.38", "3.86.7.50"]
env.user = "ubuntu"
env.key_filename = "~/.ssh/school"

def do_deploy(archive_path):
    """
    Deploy the web files to the server.

    Args:
        archive_path (str): Path to the archive file to be deployed.

    Returns:
        bool: True if deployment is successful, False otherwise.
    """
    try:
        # Check if the archive file exists
        if not (path.exists(archive_path)):
            return False

        # Transfer the archive file to the remote server
        put(archive_path, "/tmp/")

        # Extract the archive file to a specific directory
        timestamp = archive_path[-18:-4]
        run(
            "sudo mkdir -p /data/web_static/\
releases/web_static_{}/".format(
                timestamp
            )
        )
        run(
            "sudo tar -xzf /tmp/web_static_{}.tgz -C \
/data/web_static/releases/web_static_{}/".format(
                timestamp, timestamp
            )
        )

        # Remove the temporary archive file
        run("sudo rm /tmp/web_static_{}.tgz".format(timestamp))

        # Move the extracted content to its destination
        run(
            "sudo mv /data/web_static/releases/web_static_{}/web_static/* \
/data/web_static/releases/web_static_{}/".format(
                timestamp, timestamp
            )
        )

        # Remove the previous symbolic link
        run(
            "sudo rm -rf /data/web_static/releases/\
web_static_{}/web_static".format(
                timestamp
            )
        )

        # Update the symbolic link to point to the new deployment
        run("sudo rm -rf /data/web_static/current")
        run(
            "sudo ln -s /data/web_static/releases/\
web_static_{}/ /data/web_static/current".format(
                timestamp
            )
        )
    except Exception as e:
        return False

    return True

