#!/usr/bin/python3
'''Fabric script that generates a .tgz archive from the contents of the web_static'''


from fabric.api import run, local
from datetime import datetime

def do_pack():
    '''unctin abric that generates a .tgz archive'''
    run(mkdir -p /version)
    tarf = "tar cvzf version/web_static_{}.tgz /data/web_static/".format(datetime().now().strftime("%Y%m%d%H%M%S"))
    local(/version/tarf)
