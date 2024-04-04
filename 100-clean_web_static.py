#!/usr/bin/python3
"""deletes out-of-date archives, using the function do_clean"""
import os
from fabric.api import *

env.hosts = ['54.160.84.85', '54.157.163.209']


def do_clean(number=0):
    """deletes out-of-date archives"""
    number = 1 if int(number) == 0 else int(number)

    arch = sorted(os.listdir("versions"))
    [arch.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(x)) for x in arch]

    with cd("/data/web_static/releases"):
        arch = run("ls -tr").split()
        arch = [x for x in arch if "web_static_" in x]
        [arch.pop() for i in range(number)]
        [run("rm -rf ./{}".format(x)) for x in arch]
