#!/usr/bin/python3
<<<<<<< HEAD
"""
Deletes out-of-date archives
fab -f 100-clean_web_static.py do_clean:number=2
    -i ssh-key -u ubuntu > /dev/null 2>&1
"""

import os
from fabric.api import *

env.hosts = ['52.87.155.66', '54.89.109.87']
=======
# Fabfile to delete out-of-date archives.
import os
from fabric.api import *

env.hosts = ["104.196.168.90", "35.196.46.172"]
>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625


def do_clean(number=0):
    """Delete out-of-date archives.
<<<<<<< HEAD
    Args:
        number (int): The number of archives to keep.
=======

    Args:
        number (int): The number of archives to keep.

>>>>>>> 8dce1f35a43b2c2bb664ec01f78bfef42b605625
    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the most and second-most recent archives,
    etc.
    """
    number = 1 if int(number) == 0 else int(number)

    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
