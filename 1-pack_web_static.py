#!/usr/bin/python3
""" generates a .tgz archive from the contents of the web_static"""
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """generates a .tgz archive"""
    current_time = datetime.utcnow()
    arch = "versions/web_static_{}{}{}{}{}{}.tgz".format(current_time.year,
                                                         current_time.month,
                                                         current_time.day,
                                                         current_time.hour,
                                                         current_time.minute,
                                                         current_time.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return arch
