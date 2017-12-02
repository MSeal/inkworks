import os
import sys
from setuptools import setup

python_2 = sys.version_info[0] == 2
def read(fname):
    with open(fname, 'rU' if python_2 else 'r') as fhandle:
        return fhandle.read()

version = '0.1.0'
required = [req.strip() for req in read('requirements.txt').splitlines() if req.strip()]
setup(
    name='ink',
    version=version,
    author='Matthew Seal',
    author_email='mseal007@gmail.com',
    description='An ',
    install_requires=required,
    license='MIT',
    packages=['squidroom'],
    test_suite='tests',
    zip_safe=False,
    url='https://github.com/MSeal/inkworks',
    download_url='https://github.com/MSeal/inkworks/tarball/v' + version,
    keywords=['sensors', 'raspberry_pi', 'scripting', 'octoprint'],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.7'
    ]
)
