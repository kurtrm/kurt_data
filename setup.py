"""Setup for kurt's data set analysis."""
from setuptools import setup


extra_packages = {
    'testing': ['pytest', 'pytest-cov', 'tox']
}


setup(
    name='Kurt Data',
    description='Application for downloading sources of personal data.',
    version=0.0,
    author='Kurt Maurer',
    author_email='kurtrm@gmail.com',
    license='MIT',
    install_requires=['fitbit', 'PyPDF2'],
    extras_require=extra_packages
)
