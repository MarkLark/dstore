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


Javascript Client
=================

Flask-DStore provides a javascript library that allows you to easily create, read, update and
delete model instances within Javascript, for every Model type registered, a Factory class
is created.

To include this library, add the following to your base html template

.. code-block:: html

    <script src="/dstore-client.js"></script>
    <script src="/dstore-models.js"></script>
    <script src="/dstore-view.js"></script>

DS.Factory
----------
This Factory contains the following methods:

.. js:class:: DS.Factory()

    .. js:function:: load_all()

        Load all Model instances from the server into browser memory

    .. js:function:: load(id)

        Load a specific Model Instance from the server into the browser memory

        :param int id: The instance ID to retrieve

    .. js:function:: get(id)

        Get a Model Instance from browser memory, null if it doesn't exist

        :param int id: The instance ID to retrieve

    .. js:function:: add(args)

        Add a new Model Instance into browser memory.

        You need to execute save on the returned object to save the instance to the server.

        :param args: A dictionary of values to store in the Model Instance

DS.Model
--------
The Model class is as follows:

.. js:class:: DS.Model()

    .. js:function:: save()

        Save this Model Instance to the Server.

    .. js:function:: delete()

        Delete the Model Instance from the server, and local browser memory.

Example Usage
-------------
You don't directly use the DS.Factory and DS.Model class' directly. Instead Flask-DStore generates instances of these class' for every Model type registered.

These are then stored under the 'ds' namespace, proceeded by the namespace of the Model types.

The following are examples of how to use this library with the following Model:

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

Load All
~~~~~~~~

.. code-block:: js

    ds.cars.make.load_all();
    car = ds.cars.make.add({ manufacturer: "Holden", make: "Commodore", year: 2010 });
    car.save();

Create
~~~~~~

.. code-block:: js

    ds.cars.make.load_all();
    car = ds.cars.make.add({ manufacturer: "Holden", make: "Commodore", year: 2010 });
    car.save();

Update
~~~~~~

.. code-block:: js

    ds.cars.make.load_all();
    car = ds.cars.make.get(1);
    car.year = 2011;
    car.save();

Delete
~~~~~~

.. code-block:: js

    ds.cars.make.load_all();
    car = ds.cars.make.get(1);
    car.delete();
