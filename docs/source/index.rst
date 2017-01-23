.. DStore documentation master file, created by
   sphinx-quickstart on Mon Jan 23 13:19:48 2017.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to DStore!
==================

DStore (DataStore) is a Python Object Relational Mapper (ORM) that allows easy description of data models.

The source code can be found on GitHub at `https://github.com/MarkLark/dstore <https://github.com/MarkLark/dstore>`_

The Python Package can be found on PyPi at `https://pypi.python.org/pypi/DStore <https://pypi.python.org/pypi/DStore>`_

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

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   introduction
   models
   crud
   modules

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
