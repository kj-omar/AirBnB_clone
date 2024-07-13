#!/usr/bin/python3
""" Fabric script that  creates and distributes an archive
to  web servers
"""
import os
from fabric.api import local, env, put, sudo
import datetime
pack = __import__("1-pack_web_static")
dep = __import__("2-do_deploy_web_static")

hosts = ['100.26.152.53', '35.174.208.133']


def deploy():
    """ function handle full deployment """
    path = pack.do_pack()
    if path is not None:
        for host in hosts:
            env.host_string = host
            result = dep.do_deploy(path)
        return result
    return False
