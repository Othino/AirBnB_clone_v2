#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import env, run


env.hosts = ['<52.3.41.70 web-01>', '<52.86.37.174 web-02>']


def do_clean(number=0):
    """Delete all unnecessary archives (all archives minus the number to keep)
    in the versions folder and the /data/web_static/releases folder of both of
    your web servers
    
    Args:
    number: int: number of the archives, including the most recent, to keep.
    If number is 0 or 1, keep only the most recent version of your archive.
    if number is 2, keep the most recent, and second most recent versions of your archive.
    """
    if number == 0:
        number = 1
    archive_list = run("ls -1t /data/web_static/releases/").split()
    to_delete = archive_list[number:]
    if to_delete:
        for archive in to_delete:
            run(f"rm -rf /data/web_static/releases/{archive}")
            run(f"rm -rf /versions/{archive}")
        print(f"Deleted archives: {to_delete}")
    else:
        print("No archives to delete.")
