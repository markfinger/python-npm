import os
import subprocess
from .exceptions import NpmInstallArgumentsError
from .conf import settings
from .interrogate import (
    npm_installed, npm_version, npm_version_raw, raise_if_npm_missing, raise_if_npm_version_less_than, run_command
)


def ensure_npm_installed():
    raise_if_npm_missing()


def ensure_npm_version_gte(required_version):
    ensure_npm_installed()
    raise_if_npm_version_less_than(required_version)


def npm_run(*args):
    ensure_npm_installed()
    return run_command((settings.PATH,) + tuple(args))


def npm_install(target_dir):
    if not target_dir or not os.path.exists(target_dir) or not os.path.isdir(target_dir):
        raise NpmInstallArgumentsError(
            'npm.install\'s `target_dir` parameter must be a string pointing to a directory. Received "{0}"'.format(
                target_dir
            )
        )

    ensure_npm_installed()

    command = (settings.PATH, settings.INSTALL_COMMAND)

    if settings.INSTALL_PATH_TO_PYTHON:
        command += ('--python={path_to_python}'.format(path_to_python=settings.INSTALL_PATH_TO_PYTHON),)

    subprocess.call(command, cwd=target_dir)