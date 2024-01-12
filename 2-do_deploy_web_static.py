#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the web_static'''
from fabric.api import local, put
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

def do_deploy(archive_path):
        archive_path = f"versions/web_static_{time}.tgz"
        put(archive_path /tmp/)
        res = "tar xvzf /data/web_static/releases/ 
