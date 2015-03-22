from setuptools import setup, find_packages
import npm

setup(
    name='python-npm',
    version=npm.VERSION,
    packages=find_packages(exclude=('tests',)),
    description='Python bindings and utils for npm.',
    long_description='Documentation at https://github.com/markfinger/python-npm',
    author='Mark Finger',
    author_email='markfinger@gmail.com',
    url='https://github.com/markfinger/python-npm',
)