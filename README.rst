Welcome To DStore
#################

.. image:: https://img.shields.io/coveralls/MarkLark/dstore.svg
    :target: https://coveralls.io/github/MarkLark/dstore?branch=master

.. image:: https://img.shields.io/travis/MarkLark/dstore/master.svg
    :target: https://travis-ci.org/MarkLark/dstore

.. image:: https://img.shields.io/pypi/v/dstore.svg
    :target: https://pypi.python.org/pypi/dstore

.. image:: https://img.shields.io/pypi/pyversions/dstore.svg
    :target: https://pypi.python.org/pypi/dstore

DStore (DataStore) is a Python Object Relational Mapper (ORM) that allows easy description of data models.

Installing
==========

From PyPi
---------
DStore is available from the PyPi repository at `DStore <https://pypi.python.org/pypi/DStore>`_.

This means that all you have to do to install DStore is run the following in a console:

.. code-block:: console

    $ pip install dstore

From Source
-----------
DStore can also be installed from source by downloading from GitHub and running setup.py.

.. code-block:: console

    $ wget https://github.com/MarkLark/dstore/archive/master.tar.gz
    $ tar xvf master.tar.gz
    $ cd dstore-master
    $ python setup.py install


Requirements
============
DStore does not rely on any other Python Packages.

It has also been thoroughly tested to work on the following Python Versions:

* 2.7
* 3.3
* 3.4
* 3.5
* 3.6

Minimal Example
===============

.. code-block:: python

    from dstore import MemoryStore, Model, var, mod

    class Car( Model ):
        _namespace = "cars.make"
        _vars = [
            var.RowID,
            var.String( "manufacturer", 32, mods = [ mod.NotNull() ] ),
            var.String( "make", 32, mods = [ mod.NotNull() ] ),
            var.Number( "year", mods = [ mod.NotNull(), mod.Min( 1950 ), mod.Max( 2017 ) ] ),
        ]

    # Create the MemoryStore instance, and add Models to it
    store = MemoryStore( [ Car ] )
    store.init_app()
    store.connect()
    store.create_all()

    # Create a new Car, then retrieve it using filter and all
    Car( manufacturer = "Holden", make = "Commodore", year = 2010 ).add()
    holdens = Car.filter( manufacturer = "Holden" )
    cars = Car.all()

    # Destroy all instances and shut down the application
    store.destroy_all()
    store.disconnect()
    store.destroy_app()


Documentation: `ReadTheDocs <http://python-dstore.readthedocs.io/>`_

Test Results: `Travis CI <https://travis-ci.org/MarkLark/dstore>`_

Test Coverage: `Coveralls <https://coveralls.io/github/MarkLark/dstore>`_
