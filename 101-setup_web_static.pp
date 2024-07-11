#!/usr/bin/python3
import os
from fabric.api import *

env.hosts = ['100.25.19.204', '54.157.159.85']

def do_clean(number=0):
    """Remove outdated archives.

    Args:
        number (int): The number of archives to retain.

    If number is 0 or 1, keeps only the most recent archive. If
    number is 2, keeps the two most recent archives, and so on.
    """
    number = 1 if int(number) == 0 else int(number)

    # List and sort archives in the versions directory
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    
    # Remove older archives locally
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    # Remove older archives on the remote server
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
