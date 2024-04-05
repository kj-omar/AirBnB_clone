#!/usr/bin/python3
"""
This script generates a compressed .tgz archive
from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Compresses files within the web_static folder
    into a .tgz archive with a timestamp in its name.
    """
    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    # Compress web_static folder into a .tgz archive
    timestamp = datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
    result = local(f"tar -czvf versions/web_static_{timestamp}.tgz web_static", capture=True)

    # Check if compression was successful
    if result.failed:
        return None
    return result

