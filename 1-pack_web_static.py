#!/usr/bin/python3
""" Fabric script that generates a .tgz archive from the contents of the web_static
"""

from fabric.api import *
import datetime

def do_pack():
    """ function to create  .tgz archive """

    local("mkdir -p versions")
    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    archive_name = "versions/web_static_{}.tgz".format(time_stamp))
    res = local("tar -czf {} web_static".format(archive_name))
    if res.succeeded:
        return archive_name
    else:
        return None


