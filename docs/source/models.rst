Models
######

Models are used to describe the data types you wish to use.

Base Model
==========
The base model

Variables
=========
Variables within a Model

.. module:: dstore.var

.. autoclass:: Variable
    :members:

RowID
-----
RowID denotes an instance ID, and is not a Class but an instance of dstore.var.Number:

.. code-block:: python

    from dstore import var, mod
    RowID = Number( "id", mods = [ mod.AutoIncrement(), mod.PrimaryKey(), mod.Unique() ])

In terms of a MySQL it equates to:

.. code-block:: sql

    id INT NOT NULL AUTO_INCREMENT,
    UNIQUE (id),
    PRIMARY KEY (id)

Usage

.. code-block:: python

    from dstore import Model, var

    class Car( Model ):
        _namespace = "cars.make"
        _vars = [
            var.RowID
        ]

Number
------
.. autoclass:: Number

Boolean
-------
.. autoclass:: Boolean

Character
---------
.. autoclass:: Character

Binary
------
.. autoclass:: Binary

String
------
.. autoclass:: String

Text
----
.. autoclass:: Text

Float
-----
.. autoclass:: Float

Enum
----
.. autoclass:: Enum

ForeignKey
----------
.. autoclass:: ForeignKey

Date
----
.. autoclass:: Date

Time
----
.. autoclass:: Time

DateTime
--------
.. autoclass:: DateTime


Modifiers
=========
.. module:: dstore.mod

.. autoclass:: Mod
    :members:

PrimaryKey
----------
.. autoclass:: PrimaryKey

NotNull
-------
.. autoclass:: NotNull
    :members:

AutoIncrement
-------------
.. autoclass:: AutoIncrement

Unique
------
.. autoclass:: Unique

ForeignKey
----------
.. autoclass:: ForeignKey

Min
---
.. autoclass:: Min
    :members:

Max
---
.. autoclass:: Max
    :members:

Length
------
.. autoclass:: Length
    :members:

InEnum
------
.. autoclass:: InEnum
    :members:
