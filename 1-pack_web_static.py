#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the web_static'''
from fabric.api import local
from datetime import datetime


def do_pack():
        '''unctin abric that generates a .tgz archive'''
        time = datetime.now().strftime("%Y%m%d%H%M%S")
        tarre = "tar cvzf versions/web_static_{}.tgz web_static".format(time)
        local("mkdir -p versions")
        res = local(tarre)
        if res.failed:
            return None
        return f"versions/web_static_{time}.tgz"
