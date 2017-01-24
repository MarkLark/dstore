Events
######

.. contents:: Table of Contents

Introduction
============
DStore makes the use of an Event Manager in the Store and Models themselves.

These events allow you to hook custom code before or after an action takes place.

In fact, this is exactly how DStore-ACL works to provide a security layer to DStore Models.

Listening To Events
-------------------
Listening to an event is as easy as adding your method to the event in question.

For example, to listen to before_init_app on the store:

.. code-block:: python

    from dstore import MemoryStore

    def before_init_app( event, store ):
        print( "Before init store %s" % store.name )

    def after_init_app( event, store ):
        print( "After init store %s" % store.name )

    store = MemoryStore()
    store.events.before_init_app += before_init_app
    store.events.after_init_app  += after_init_app

    store.init_app()


Store Events
============
To listen to a store event, you add your method to the store's event object.

.. code-block:: python

    store.events.before_init_app += method_to_call

init_app
--------
This event is fired before and after you execute store.init_app()

.. py:function:: before_init_app( event, store )
                 after_init_app( event, store )

    .. py:attribute:: store

        The Data Store that init_app is being run on

destroy_app
-----------
This event is fired before and after you execute destroy_app on a store

.. py:function:: before_destroy_app( event, store )
                 after_destroy_app( event, store )

    .. py:attribute:: store

        The Data Store that destroy_app is being run on

register_models
---------------
This event is fired before and after all models have been registered.

This happens automatically when init_app is run on the store

.. py:function:: before_register_models( event, store )
                 after_register_models( event, store )

    .. py:attribute:: store

        The Data Store that register_models is being run on

register_model
--------------
This event is fired when a single Model is being registered on the store.

.. py:function:: before_register_models( event, store, model )
                 after_register_models( event, store, model )

    .. py:attribute:: store

        The Data Store that register_models is being run on

    .. py:attribute:: model

        The Model Class that is being registered

create_all
----------
This event is fired before and after you execute create_all on a store

.. py:function:: before_create_all( event, store )
                 after_create_all( event, store )

    .. py:attribute:: store

        The Data Store that create_all is being run on

destroy_all
-----------
This event is fired before and after you execute destroy_all on a store

.. py:function:: before_destroy_all( event, store )
                 after_destroy_all( event, store )

    .. py:attribute:: store

        The Data Store that destroy_all is being run on

empty_all
---------
This event is fired before and after you execute empty_all on a store

.. py:function:: before_empty_all( event, store )
                 after_empty_all( event, store )

    .. py:attribute:: store

        The Data Store that empty_all is being run on

connect
-------
This event is fired before and after you execute connect on a store

.. py:function:: before_connect( event, store )
                 after_connect( event, store )

    .. py:attribute:: store

        The Data Store that connect is being run on

disconnect
----------
This event is fired before and after you execute disconnect on a store

.. py:function:: before_disconnect( event, store )
                 after_disconnect( event, store )

    .. py:attribute:: store

        The Data Store that disconnect is being run on


Model Events
============
To listen to a store event, you add your method to the store's event object.

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

    def car_before_add( event, model, instance ):
        print( "Attempting to add a new %s instance" % model._namespace )

    Car.events.before_add += car_before_add

add
---
This event is fired before and after you attempt to add a new Model Instance

.. py:function:: before_add( event, model, instance )
                 after_add( event, model, instance )

    .. py:attribute:: model

        The Model Class that a new instance is being added to

    .. py:attribute:: instance

        The instance that is attempting to be added to the Model Class storage

delete
------
This event is fired before and after you attempt to delete an existing Model Instance

.. py:function:: before_delete( event, model, instance )
                 after_delete( event, model, instance )

    .. py:attribute:: model

        The Model Class of the instance to be deleted

    .. py:attribute:: instance

        The instance that is attempting to be deleted from the Model Class storage

update
------
This event is fired before and after you attempt to update an existing Model Instance

.. py:function:: before_update( event, model, instance )
                 after_update( event, model, instance )

    .. py:attribute:: model

        The Model Class of the instance to be updated

    .. py:attribute:: instance

        The instance that is attempting to be updated

validate
--------
This event is fired before and after you attempt to add or update a Model Instance (i.e. on validation)

.. py:function:: before_validate( event, model, instance )
                 after_validate( event, model, instance )

    .. py:attribute:: model

        The Model Class of the instance to be added or updated

    .. py:attribute:: instance

        The instance that is attempting to be added or updated

all
---
This event is fired before and after you attempt to get all Model instances

.. py:function:: before_all( event, model )

    .. py:attribute:: model

        The Model Class of the instance to be added or updated

.. py:function:: after_all( event, model, instances )

    .. py:attribute:: model

        The Model Class of the instance to be added or updated

    .. py:attribute:: instances

        The list of all instances

get
---
This event is fired before and after you attempt to get a Model instance

.. py:function:: before_get( event, model, row_id )

    .. py:attribute:: model

        The Model Class of the instance to be added or updated

    .. py:attribute:: row_id

        The ID of the instance to retrieve

.. py:function:: after_get( event, model, instance )

    .. py:attribute:: model

        The Model Class of the instance to be added or updated

    .. py:attribute:: instance

        The Model instance retrieved

empty
-----
This event is fired before and after you attempt to delete all Model instances

.. py:function:: before_empty( event, model )
                 after_empty( event, model )

    .. py:attribute:: model

        The Model Class that is to be emptied

create
------
This event is fired before and after you attempt to create the storage for the Model instances

.. py:function:: before_create( event, model )
                 after_create( event, model )

    .. py:attribute:: model

        The Model Class that storage is to be created for

destroy
-------
This event is fired before and after you attempt to destroy the storage for the Model instances

.. py:function:: before_destroy( event, model )
                 after_destroy( event, model )

    .. py:attribute:: model

        The Model Class that storage is to be destroyed for

filter
------
This event is fired before and after you attempt to get a filtered list of the Model instances

.. py:function:: before_filter( event, model, params )

    .. py:attribute:: model

        The Model Class to filter for instances

    .. py:attribute:: params

        A dictionary of the parameters used to filter the list

.. py:function:: after_filter( event, model, instances, params )

    .. py:attribute:: model

        The Model Class to filter for instances

    .. py:attribute:: instances

        The filtered list of Model instances

    .. py:attribute:: params

        A dictionary of the parameters used to filter the list