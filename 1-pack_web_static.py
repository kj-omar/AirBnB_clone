#/usr/bin/python3

from fabric import task
from datetime import datetime
import os

def do_psck()
if not os.path.isdir("versions"):
        os.mkdir("versions")

    # Get the current date and time
    d_time = datetime.now()

    output = f"versions/web_static_{d_time.year}{d_time.month}{d_time.day}{d_time.hour}{d_time.minute}{d_time.second}.tgz"

	 try:
        # Create the archive
        print("Packing web_static to {}".format(output))
        c.local("tar -cvzf {} web_static".format(output))

        # Get the size of the archive
        size = os.stat(output).st_size
        print("web_static packed: {} -> {} Bytes".format(output, size))
    except Exception as e:
        print("Error packing web_static:", str(e))
        output = None

    return output
