from .Error import ValidationError


class Mod( object ):
    """
    The base class used for creating a Modifier.

    A Modifier is a way to validate Model instance Variables upon add and/or update.
    """
    type = ""

    def validate( self, instance, var, val ):
        """

        :param instance: The Model instance
        :param var: The Model Variable Class
        :param val: The Model instance variable
        :return: If not a valid value, an exception of dstore.Error.ValidationError will be raised
        """
        pass


class PrimaryKey( Mod ):
    """
    This modifier specifies that the variable is used as a Model ID.

    This is automatically used by dstore.val.RowID.
    """
    type = "PrimaryKey"


class NotNull( Mod ):
    """
    This modifier ensures that the value is not None.
    """
    type = "NotNull"

    class NotNull_Error( ValidationError ): pass

    def validate( self, instance, var, val ):
        """
        :raises: Raises dstore.mod.NotNull.NotNull_Error if val is None
        """
        if val is None:
            raise NotNull.NotNull_Error(
                instance,
                var,
                val,
                self,
                "Variable must have a value assigned to it"
            )


class AutoIncrement( Mod ):
    """
    This modifier specifies that the variable is automatically incremented.

    This is automatically used by dstore.val.RowID.
    """
    type = "AutoIncrement"


class Unique( Mod ):
    """
    This modifier ensures that the value is unique to all other instances.
    """
    type = "Unique"


class ForeignKey( Mod ):
    """
    This modifier specifies that the value references another Model instance.

    This is automatically used by dstore.val.ForeignKey.
    """
    type = "ForeignKey"

    def __init__( self, namespace ):
        self.namespace = namespace


class Min( Mod ):
    """
    This modifier ensures that the value is greater than a specific number.

    :param value: The minimum value allowed
    """
    type = "Min"

    class Min_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
        """
        :raises: Raises dstore.mod.Min.Min_Error if val is less than the allowed number.
        """
        if val is None: return
        if val < self.value:
            raise Min.Min_Error(
                instance,
                var,
                val,
                self,
                "Variable must not be less than %d" % self.value
            )


class Max( Mod ):
    """
    This modifier ensures that the value is less than a specific number.

    :param value: The maximum value allowed
    """
    type = "Max"

    class Max_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
        """
        :raises: Raises dstore.mod.Max.Max_Error if val is greater than the allowed number.
        """
        if val is None: return
        if val > self.value:
            raise Max.Max_Error(
                instance,
                var,
                val,
                self,
                "Variable must not be greather than %d" % self.value
            )


class Length( Mod ):
    """
    This modifier ensures that the value does not exceed the given length.

    :param value: The maximum length of the value allowed
    """
    type = "Length"

    class Length_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
        """
        :raises: Raises dstore.mod.Length.Length_Error if the length of the value exceed the allowed size.
        """
        if val is None: return
        val_len = len( val )
        if val_len > self.value:
            raise Length.Length_Error(
                instance,
                var,
                val,
                self,
                "Data length %d exceeds upper limit of %d" % ( val_len, self.value )
            )


class InEnum( Mod ):
    """
    This modifier ensures that the value exists in the enumerated list.

    This is automatically used by :py:class:`dstore.val.Enum`.

    :param value: A list of the allowed values
    """
    type = "InEnum"

    class InEnum_Error( ValidationError ): pass

    def __init__( self, values ):
        self.values = values

    def validate( self, instance, var, val ):
        """
        :raises: Raises dstore.mod.InEnum.InEnum_Error if the value does not exist in the enumerated list.
        """
        if val is None: return
        if val not in self.values:
            raise InEnum.InEnum_Error(
                instance,
                var,
                val,
                self,
                "Value %s is not in enum" % var
            )
