#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Creates a .tgz file"""
    time = datetime.now().strftime("%Y%m%d%H%M%S")
    name = f"web_static_{time}.tgz"
    local("mkdir -p ./versions")
    local(f"tar -czvf ./versions/{name} ./web_static")
