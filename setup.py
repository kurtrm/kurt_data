"""Setup for transcript transcriber."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest-cov', 'tox']
}


setup(
    name='Transcript Transcriber',
    description='Passes security credentials to the UF website'
                'and parses unofficial transcripts to look nicer.',
    version=0.0,
    author='Kurt Maurer',
    author_email='kurtrm@gmail.com',
    license='MIT',
    install_requires=['bs4', 'requests', 'pytest'],
    extras_require=extra_packages
)