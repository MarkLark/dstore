from . import mod


class Variable( object ):
    """
    The base class used for creating Variable types
    This also provides a validate method which iterates over the
    modifiers and runs their validate method on this variable instance.

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()
    """
    type = None

    def __init__( self, name, default = None, mods = None ):
        self.name    = name
        self.default = default
        self._mods   = mods

        if self._mods is None: self._mods = []

    def validate( self, instance ):
        """
        Validate the value of an instance of this Variable type (this is used by the dstore.Model.validate method)

        :param instance: The instance of this variable type
        :return: If not a valid value, an exception of dstore.Error.ValidationError will be raised
        """
        val = instance.__dict__[ self.name ]
        for m in self._mods:
            m.validate( instance, self, val )


class Number( Variable ):
    """
    This variable type is used to store an integer value.

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var, mod
        var.Number( "year", 1950, mods = [ mod.NotNull() ] )
    """
    type = "Number"


class Boolean( Variable ):
    """
    This variable is used to store a boolean value.

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.Boolean( "is_available", False )
    """
    type = "Boolean"


class Character( Variable ):
    """
    This variable is used to store a string of static length.

    :param name: The name of the Variable instance inside a Model Class
    :param length: The length of the string
    :param default: The default value to give this variable
    :param mods: A list of modifiers. The mod dstore.mod.Length( length ) is always added to this list

    Usage:

    .. code-block:: python

        from dstore import var
        var.Character( "is_available", 4 )
    """
    type = "Character"

    def __init__( self, name, length, default = None, mods = None ):
        super( Character, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class Binary( Variable ):
    """
    This variable is used to store binary data.

    :param name: The name of the Variable instance inside a Model Class
    :param length: The length of the data
    :param default: The default value to give this variable
    :param mods: A list of modifiers. The mod dstore.mod.Length( length ) is always added to this list

    Usage:

    .. code-block:: python

        from dstore import var
        var.Binary( "data", 32 )
    """
    type = "Binary"

    def __init__( self, name, length, default = None, mods = None ):
        super( Binary, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class String( Variable ):
    """
    This variable is used to store a string of variable length.

    :param name: The name of the Variable instance inside a Model Class
    :param length: The length of the string
    :param default: The default value to give this variable
    :param mods: A list of modifiers. The mod dstore.mod.Length( length ) is always added to this list

    Usage:

    .. code-block:: python

        from dstore import var
        var.String( "username", 32 )
    """
    type = "String"

    def __init__( self, name, length, default = None, mods = None ):
        super( String, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class Text( Variable ):
    """
    This variable is used to store text.

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.Text( "description" )
    """
    type = "Text"


class Float( Variable ):
    """
    This variable is used to store a floating point integer.

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.Float( "price" )
    """
    type = "Float"


class Enum( Variable ):
    """
    This variable is used to store a an enum.

    :param name: The name of the Variable instance inside a Model Class
    :param values: The list of available choices
    :param default: The default value to give this variable
    :param mods: A list of modifiers. The mod dstore.mod.InEnum( values ) is always added to this list

    Usage:

    .. code-block:: python

        from dstore import var
        var.Enum( "car_type", [ "truck", "bus", "ute", "car", "motorbike" ], mods = [ mod.NotNull() ] )
    """
    type = "Enum"

    def __init__( self, name, values, default = None, mods = None ):
        super( Enum, self ).__init__( name, default, mods )
        self.values = values
        self._mods.append( mod.InEnum( values ) )


class ForeignKey( Number ):
    """
    This variable is used to link the Model Instance to another Model Instance

    :param namespace: The namespace of the Model Class this variable references

    This variable type is a subclass of dstore.var.Number, with the following mods:

    * dstore.mod.NotNull
    * dstore.mod.ForeignKey

    The name given to this variable is the name of the Model Class being referenced with a suffix of '_id"

    For example:

    .. code-block:: python

        from dstore import var
        var.ForeignKey( "cars.make" )

    Is similar to:

    .. code-block:: python

        from dstore import var
        var.Number( "cars_make_id", mods = [ dstore.mod.NotNull(), dstore.mod.ForeignKey( "cars.make" ) )
    """
    type = "ForeignKey"

    def __init__( self, namespace ):
        super( ForeignKey, self ).__init__( "%s_id" % namespace.replace( ".", "_" ), mods = [ mod.NotNull(), mod.ForeignKey( namespace ) ] )


class Date( Variable ):
    """
    This variable is used to store a date value (without a timezone offset).

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.Date( "build_date" )
    """
    type = "Date"


class Time( Variable ):
    """
    This variable is used to store a time value (without a timezone offset).

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.Time( "build_time" )
    """
    type = "Time"


class DateTime( Variable ):
    """
    This variable is used to store a date and time value (without a timezone offset).

    :param name: The name of the Variable instance inside a Model Class
    :param default: The default value to give this variable
    :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

    Usage:

    .. code-block:: python

        from dstore import var
        var.DateTime( "built_on" )
    """
    type = "DateTime"

RowID = Number( "id", mods = [ mod.AutoIncrement(), mod.PrimaryKey(), mod.Unique() ] )
