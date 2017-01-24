Events
######

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

add
---
This event is fired before and after you attempt to add a new Model Instance

.. py:function:: before_disconnect( event, model, instance )
                 after_disconnect( event, model, instance )

    .. py:attribute:: model

        The Model Class that a new instance is being added to

    .. py:attribute:: instance

        The instance that is attempting to be added to the Model Class storage