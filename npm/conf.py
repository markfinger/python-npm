from optional_django.conf import Conf

settings = Conf('NPM', {
    'PATH': 'npm',
    'VERSION_COMMAND': '--version',
    'VERSION_FILTER': lambda version: tuple(map(int, version.split('.'))),
    'INSTALL_COMMAND': 'install',
    'INSTALL_PATH_TO_PYTHON': None,
})