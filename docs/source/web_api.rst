Web API - Flask-DStore
######################
.. image:: https://img.shields.io/coveralls/MarkLark/flask-dstore.svg
    :target: https://coveralls.io/github/MarkLark/flask-dstore?branch=master

.. image:: https://img.shields.io/travis/MarkLark/flask-dstore/master.svg
    :target: https://travis-ci.org/MarkLark/flask-dstore

.. image:: https://img.shields.io/pypi/v/flask-dstore.svg
    :target: https://pypi.python.org/pypi/flask-dstore

.. image:: https://img.shields.io/pypi/pyversions/flask-dstore.svg
    :target: https://pypi.python.org/pypi/flask-dstore

Introduction
============
Flask-DStore is a Web API and Javascript Client.

The API routes, logic and client code is automatically generated for you.

Installing
==========
You have two choices to install dstore-mysql, using pip or from source.

From PyPi
---------
DStore is available from the PyPi repository at `https://pypi.python.org/pypi/flask-dstore <https://pypi.python.org/pypi/flask-dstore>`_.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install flask-dstore

From Source
-----------
DStore can also be installed from source by downloading from GitHub and running setup.py.

.. code-block:: console

    $ wget https://github.com/MarkLark/flask-dstore/archive/master.tar.gz
    $ tar xvf master.tar.gz
    $ cd flask-dstore-master
    $ python setup.py install


Minimal Example
===============

.. code-block:: python

    from flask import Flask
    from dstore import MemoryStore, Model, var, mod
    from flask_dstore import API

    class Car( Model ):
        _namespace = "cars.make"
        _vars = [
            var.RowID,
            var.String( "manufacturer", 32, mods = [ mod.NotNull() ] ),
            var.String( "make", 32, mods = [ mod.NotNull() ] ),
            var.Number( "year", mods = [ mod.NotNull(), mod.Min( 1950 ), mod.Max( 2017 ) ] ),
        ]

    # Create the app instances
    app = Flask( __name__ )
    store = MemoryStore( [ Car ] )
    api = API( store, app )

    # While inside the Flask app context, create all storage and add a car
    with app.app_context():
        store.create_all()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()

    # Run the Flask dev. server
    app.run()

    # Now destroy all data
    with app.app_context():
        store.destroy_all()

    store.destroy_app()
