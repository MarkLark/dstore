Models
######

Models are used to describe the data types you wish to use.

Base Model
==========
The base model

Variables
=========
Variables within a Model

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
This variable is used to store an integer value.

.. module:: dstore.var

.. autoclass:: Number

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

Usage:

.. code-block:: python

    from dstore import var, mod
    var.Number( "year", 1950, mods = [ mod.NotNull() ] )

Boolean
-------
This variable is used to store a boolean value.

.. autoclass:: Boolean

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

Usage:

.. code-block:: python

    from dstore import var
    var.Boolean( "is_available", False )

Character
---------
This variable is used to store a string of static length.

.. autoclass:: Character

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: length

        The length of the string

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers.

        The mod dstore.mod.Length( length ) is always added to this list

Usage:

.. code-block:: python

    from dstore import var
    var.Character( "is_available", 4 )

Binary
------
This variable is used to store binary data.

.. autoclass:: Binary

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: length

        The length of the data

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

        The mod dstore.mod.Length( length ) is always added to this list

Usage:

.. code-block:: python

    from dstore import var
    var.Binary( "data", 32 )

String
------
This variable is used to store a string of variable length.

.. autoclass:: String

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: length

        The maximum length of the string

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

        The mod dstore.mod.Length( length ) is always added to this list

Usage:

.. code-block:: python

    from dstore import var
    var.String( "username", 32 )

Text
----
This variable is used to store text.

.. autoclass:: Text

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

Usage:

.. code-block:: python

    from dstore import var
    var.Text( "description" )

Float
-----
This variable is used to store a floating point integer.

.. autoclass:: Text

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

Usage:

.. code-block:: python

    from dstore import var
    var.Float( "price" )

Enum
----
This variable is used to store a an enum.

.. autoclass:: Enum

    .. py:attribute:: name

        The name of the variable

    .. py:attribute:: values

        The list of available choices

    .. py:attribute:: default

        The default value if none is supplied

    .. py:attribute:: mods

        A list of Variable Modifiers

        The mod dstore.mod.InEnum( values ) is always added to this list

Usage:

.. code-block:: python

    from dstore import var, mod
    var.Enum( "car_type", [ "truck", "bus", "ute", "car", "motorbike" ], mods = [ mod.NotNull() ] )

ForeignKey
----------
dstore.var.ForeignKey

Date
----
dstore.var.Date

Time
----
dstore.var.Time

DateTime
--------
dstore.var.DateTime


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
