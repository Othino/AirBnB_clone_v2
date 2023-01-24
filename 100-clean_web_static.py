#!/usr/bin/python3
"""A module for web application deployment with Fabric."""
from fabric.api import env, run


env.hosts = ['<52.3.41.70 web-01>', '<52.86.37.174 web-02>']


def do_clean(number=0):
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
