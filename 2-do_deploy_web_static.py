#!/usr/bin/python3
"""distributes an archive to your web servers, using the function do_deploy"""
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import run

env.hosts = ["54.160.84.85", "54.157.163.209"]


def do_deploy(archive_path):
    """distributes an archive to your web servers"""
    if os.path.isfile(archive_path) is False:
        return False
    arch = archive_path.split("/")[-1]
    arch_name = arch.split(".")[0]

    if put(archive_path, "/tmp/{}".format(arch)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/".
           format(arch_name)).failed is True:
        return False
    if run("mkdir -p /data/web_static/releases/{}/".
           format(arch_name)).failed is True:
        return False
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
           format(arch, arch_name)).failed is True:
        return False
    if run("rm /tmp/{}".format(arch)).failed is True:
        return False
    if run("mv /data/web_static/releases/{}/web_static/* "
           "/data/web_static/releases/{}/".format(arch_name, arch_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/releases/{}/web_static".
           format(arch_name)).failed is True:
        return False
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".
           format(arch_name)).failed is True:
        return False
    return True
