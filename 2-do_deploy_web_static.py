#!/usr/bin/python3
"""
This module deploys the web_static archive to the servers.
"""

from os.path import exists
from fabric.api import *
import shlex

env.hosts = ['54.209.221.222', '54.208.103.110']
env.user = 'ubuntu'


def do_deploy(archive_path):
    """Deploy web_static."""
    if not exists(archive_path):
        return False

    try:
        ar_name = archive_path.replace('/', ' ')
        ar_name = shlex.split(ar_name)
        ar_name = ar_name[-1]

        bare_ar_name = ar_name.replace('.', ' ')
        bare_ar_name = shlex.split(bare_ar_name)
        bare_ar_name = bare_ar_name[0]

        releases_path = "/data/web_static/releases/{}/".format(bare_ar_name)
        tmp_path = "/tmp/{}".format(ar_name)

        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except Exception:
        return False
