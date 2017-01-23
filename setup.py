from setuptools import setup
from os import path
from codecs import open

root_dir = path.abspath(path.dirname(__file__))

with open( path.join( root_dir, 'README.rst' ), encoding = 'utf-8' ) as f:
    long_description = f.read()


setup(
    name='DStore',
    version='0.1.0a1',
    url = 'https://github.com/MarkLark/dstore',
    license='MIT',
    author='Mark Pittaway',
    author_email='mark.pittaway@mlit.net.au',
    description='Python Data abstraction layer (ORM)',
    long_description=long_description,
    packages=['dstore'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'tabulate'
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
        'Topic :: Database :: Front-Ends'
    ]
)
