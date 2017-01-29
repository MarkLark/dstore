Storage
#######
DStore provides an abstraction layer to store the model instances.



MemoryStore
===========

Introduction
------------
The default storage in DStore is the MemoryStore.

This simply stores the model instances in an array in memory.

Keep in mind that this storage type is runtime only, meaning that the data is wiped when the application closes.

Usage
-----

.. code-block:: python

    from dstore import MemoryStore
    store = MemoryStore( models )

MySQLStore
==========
.. image:: https://img.shields.io/coveralls/MarkLark/dstore-mysql.svg
    :target: https://coveralls.io/github/MarkLark/dstore-mysql?branch=master

.. image:: https://img.shields.io/travis/MarkLark/dstore-mysql/master.svg
    :target: https://travis-ci.org/MarkLark/dstore-mysql

.. image:: https://img.shields.io/pypi/v/dstore-mysql.svg
    :target: https://pypi.python.org/pypi/dstore-mysql

.. image:: https://img.shields.io/pypi/pyversions/dstore-mysql.svg
    :target: https://pypi.python.org/pypi/dstore-mysql

Introduction
------------
This storage type allows model instances to be stored in a MySQL DataBase.

In order to use this storage type, you need to install the Python Package for it.

Installing
----------
You have two choices to install dstore-mysql, using pip or from source.

From PyPi
~~~~~~~~~
DStore is available from the PyPi repository at `DStore <https://pypi.python.org/pypi/DStore>`_.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install dstore-mysql

From Source
~~~~~~~~~~~
DStore can also be installed from source by downloading from GitHub and running setup.py.

.. code-block:: console

    $ wget https://github.com/MarkLark/dstore-mysql/archive/master.tar.gz
    $ tar xvf master.tar.gz
    $ cd dstore-mysql-master
    $ python setup.py install

Requirements
------------
DStore-MySQL requires the Python package `MySQL-python <https://pypi.python.org/pypi/MySQL-python/>`_.

Usage
-----

.. code-block:: python

    from dstore_mysql import MySQLStore
    store = MySQLStore( models )

MongoStore
==========
.. image:: https://img.shields.io/coveralls/MarkLark/dstore-mongo.svg
    :target: https://coveralls.io/github/MarkLark/dstore-mongo?branch=master

.. image:: https://img.shields.io/travis/MarkLark/dstore-mongo/master.svg
    :target: https://travis-ci.org/MarkLark/dstore-mongo

.. image:: https://img.shields.io/pypi/v/dstore-mongo.svg
    :target: https://pypi.python.org/pypi/dstore-mongo

.. image:: https://img.shields.io/pypi/pyversions/dstore-mongo.svg
    :target: https://pypi.python.org/pypi/dstore-mongo

Introduction
------------
This storage type allows model instances to be stored in a Mongo DataBase.

In order to use this storage type, you need to install the Python Package for it.

Installing
----------
You have two choices to install dstore-mongo, using pip or from source.

From PyPi
~~~~~~~~~
DStore-Mongo package is available from the `PyPi repository <https://pypi.python.org/pypi/DStore-Mongo>`_.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install dstore-mongo

From Source
~~~~~~~~~~~
DStore-Mongo can also be installed from source by downloading from GitHub and running setup.py.

.. code-block:: console

    $ wget https://github.com/MarkLark/dstore-mongo/archive/master.tar.gz
    $ tar xvf master.tar.gz
    $ cd dstore-mongo-master
    $ python setup.py install

Requirements
------------
DStore-Mongo requires the Python package `PyMongo <https://pypi.python.org/pypi/pymongo>`_.

Usage
-----

.. code-block:: python

    from dstore_mongo import MongoStore
    store = MongoStore( models )
