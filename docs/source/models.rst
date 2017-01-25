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
Variable Modifiers for a Model

PrimaryKey
----------
dstore.mod.PrimaryKey

NotNull
-------
dstore.mod.NotNull

AutoIncrement
-------------
dstore.mod.AutoIncrement

Unique
------
dstore.mod.Unique

ForeignKey
----------
dstore.mod.ForeignKey

Min
---
dstore.mod.Min

Max
---
dstore.mod.Max

Length
------
dstore.mod.Length

InEnum
------
dstore.mod.InEnum
