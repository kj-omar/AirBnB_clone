from fabric import task
import os

# Define the IP addresses of your web servers
env.hosts = ['100.26.138.58', '100.26.219.147']
env.user = 'ubuntu'

def do_deploy(c, archive_path):
    # Check if the archive exists
    if not os.path.exists(archive_path):
        print("Error: Archive does not exist.")
        return False

    # Upload the archive to the /tmp/ directory of the web server
    remote_archive_path = '/tmp/' + os.path.basename(archive_path)
    c.put(archive_path, remote=remote_archive_path)

    release_folder = '/data/web_static/releases/' + os.path.splitext(os.path.basename(archive_path))[0]
    c.run('sudo mkdir -p {}'.format(release_folder))
    c.run('sudo tar -xzf {} -C {}'.format(remote_archive_path, release_folder))

    c.run('sudo rm {}'.format(remote_archive_path))

    current_link = '/data/web_static/current'
    c.run('sudo rm -f {}'.format(current_link))

    c.run('sudo ln -s {} {}'.format(release_folder, current_link))

    return True
