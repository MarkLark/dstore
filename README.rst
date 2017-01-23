Welcome To DStore
#################

DStore (DataStore) is a Python Object Relational Mapper (ORM) that allows easy description of data models.


Installing
==========

PyMan is available from the PyPi repository.

This means that all you have to do to install PyMan is run the following in a console:

.. code-block:: console

    $ pip install dstore

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

    # Destroy all instances and shut down the application
    store.destroy_all()
    store.disconnect()
    store.destroy_app()


Documentation: `ReadTheDocs <http://dstore.readthedocs.io/>`_

Source Code: `GitHub <https://github.com/MarkLark/dstore>`_
