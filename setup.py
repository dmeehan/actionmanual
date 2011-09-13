from setuptools import setup, find_packages
import projects
import os

try:
    long_description = open('README.rst').read()
except IOError:
    long_description = ''

try:
    reqs = open(os.path.join(os.path.dirname(__file__), 'requirements.txt')).read()
except (IOError, OSError):
    reqs = ''

setup(
    name='actionmanual',
    version=actionmanual.get_version(),
    description='Documenting ideas and projects on vacant land',
    long_description=long_description,
    author='Douglas Meehan',
    author_email='dmeehan@gmail.com',
    include_package_data=True,
    url='http://github.com/dmeehan/actionmanual',
    packages=find_packages(),
    classifiers=[
        'Framework :: Django',
    ],
    install_requires = reqs,
    dependency_links = []
)