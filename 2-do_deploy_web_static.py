#!/usr/bin/python3
""" Fabric script distributes an archive to web servers using do_deploy
"""

from fabric.api import env, sudo, put
from os import path
from datetime import datetime


env.hosts = ['54.160.65.25, 3.90.80.134']


def do_deploy(archive_path):
    """ archive being distributed to web servers """
    try:
        if not path.exists(archive_path):
            return False
        put(archive_path, '/tmp/')
        # string slicing
        fold = archive_path[9:-4]
        rec = '/data/web_static/current'
        web_fold = '/data/web_static/releases/'

        sudo('mkdir -p {}{}'.format(web_fold, fold))
        sudo('tar -zxvf /tmp/{0}.tgz -C {1}{0}'.format(fold, web_fold))
        sudo('mv {0}{1}/web_static/* {0}{1}/*.format(web_fold, fold))

        # delete files not wanted
        sudo('rm /tmp/{}.tgz'.format(fold))
        sudo('rm -rf {0}{1}/web_static'.format(web_fold, fold))
        sudo('rm ' + rec)

        # make symbolic link to web_static folder
        sudo('ln -s {}{} {}'.format(web_fold, fold, rec))

        return True
    except Exception as e:
        return False
