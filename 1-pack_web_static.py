#!/usr/bin/python3
""" Fabric script that generates .tgz archive from the
content of web_static"""
from fabric.api import local
from datetime import datetime
from os.path import isdir


def do_pack():
    """ generates .tgz achive """
    try:
        date = datetime.now().strftime("%Y%m%d%H%M%S")
        if not isdir("versions"):
            local("mkdir versions")
        file = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file))
        return file
    except Exception as e:
        return None
