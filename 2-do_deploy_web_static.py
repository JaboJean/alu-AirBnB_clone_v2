#!/usr/bin/python3
"""
Fabric script that distributes an archive to web servers
"""

import os
from fabric.api import env, run , put
env.hosts = ['54.235.26.56', '3.92.23.222']

def do_deploy(archive_path):
    """
    Distributes an archive to web servers
    returns: True if all operations have been done correctly, 
    otherwise returns False.
    """
    if not os.path.exists(archive_path):
        return False
    try:
        file_name = archive_path.split('/')[-1]
        file_no_extension = file_name.split('.')[0]
        put(archive_path, f'/tmp/{file_name}')
        run(f'mkdir -p /data/web_static/releases/{file_no_extension}/')
        run(f"tar -xzf /tmp/{file_name} -C /data/web_static/releases/{file_no_extension}/")
        run(f'rm /tmp/{file_name}')
        run(f'mv /data/web_static/releases/{file_no_extension}/web_static/* /data/web_static/releases/{file_no_extension}/')
        run(f'rm -rf /data/web_static/releases/{file_no_extension}/web_static')
        run(f'rm -rf /data/web_static/current')
        run(f'ln -s /data/web_static/releases/{file_no_extension}/ /data/web_static/current')
        return True
    except:
        return False
