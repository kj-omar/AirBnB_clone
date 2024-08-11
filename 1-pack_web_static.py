#!/usr/bin/python3
""" Fabric script that generates a .tgz archive
"""
import os
from fabric.api import local
import datetime


def do_pack():
    """ function to create  .tgz archive """

    time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    if not os.path.exists('./versions'):
        os.mkdir('./versions')
    archive_name = "web_static_" + time_stamp
    res = local("tar -czf versions/{}.tgz web_static".format(archive_name))
    print("Packing web_static to versions/{}.tgz".format(archive_name))
    if res.succeeded:
        size = os.path.getsize("versions/{}.tgz".format(archive_name))
        print("web_static packed: versions/{}.tgz -> {}Bytes".format(
               archive_name, size))
        full_path = "versions/{}.tgz".format(archive_name)
        return full_path
    else:
        return None
