#!/usr/bin/python3
""" Fabric script that  creates and distributes an archive
to your web servers
"""
import os
from fabric.api import local, env
import datetime
pack = __import__("1-pack_web_static")
dep = __import__("2-do_deploy_web_static")

env.hosts = ['100.26.152.53', '35.174.208.133']


def deploy():
    """ function handle full deployment """

    archive_path = pack.do_pack()
    if not archive_path:
        return False

    res = dep.do_deploy(archive_path)
    return res
