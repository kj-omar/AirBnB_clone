#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from
the contents of the web_static
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """Creates a .tgz file"""

    try:
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        name = f"web_static_{time}.tgz"
        zip_path = f"versions/{name}"
        local("mkdir -p ./versions")
        local(f"tar -czvf ./versions/{name} ./web_static")
        if not (path.exists(zip_path)):
            return (False)
        return (zip_path)
    except Exception as e:
        return (None)
