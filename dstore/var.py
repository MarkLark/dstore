from . import mod


class Variable( object ):
    """
    The base class used for creating Variable types
    This also provides a validate method which iterates over the
    modifiers and runs their validate method on this variable instance.
    """
    type = None

    def __init__( self, name, default = None, mods = None ):
        """
        Construct a new Variable type

        :param name: The name of the Variable instance inside a Model Class
        :param default: The default value to give this variable
        :param mods: A list of modifiers, i.e. dstore.mod.NotNull()

        This constructs a new Variable instance
        """
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
    type = "Number"


class Boolean( Variable ):
    type = "Boolean"


class Character( Variable ):
    type = "Character"

    def __init__( self, name, length, default = None, mods = None ):
        super( Character, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class Binary( Variable ):
    type = "Binary"

    def __init__( self, name, length, default = None, mods = None ):
        super( Binary, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class String( Variable ):
    type = "String"

    def __init__( self, name, length, default = None, mods = None ):
        super( String, self ).__init__( name, default, mods )
        self.length = length
        self._mods.append( mod.Length( self.length ) )


class Text( Variable ):
    type = "Text"


class Float( Variable ):
    type = "Float"


class Enum( Variable ):
    type = "Enum"

    def __init__( self, name, values, default = None, mods = None ):
        super( Enum, self ).__init__( name, default, mods )
        self.values = values
        self._mods.append( mod.InEnum( values ) )


class ForeignKey( Number ):
    type = "ForeignKey"

    def __init__( self, namespace ):
        super( ForeignKey, self ).__init__( "%s_id" % namespace.replace( ".", "_" ), mods = [ mod.NotNull(), mod.ForeignKey( namespace ) ] )


class Date( Variable ):
    type = "Date"


class Time( Variable ):
    type = "Time"


class DateTime( Variable ):
    type = "DateTime"

RowID = Number( "id", mods = [ mod.AutoIncrement(), mod.PrimaryKey(), mod.Unique() ] )
