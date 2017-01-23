from .Error import ValidationError


class Mod( object ):
    type = ""

    def validate( self, instance, var, val ): pass


class PrimaryKey( Mod ):
    type = "PrimaryKey"


class NotNull( Mod ):
    type = "NotNull"

    class NotNull_Error( ValidationError ): pass

    def validate( self, instance, var, val ):
        if val is None:
            raise NotNull.NotNull_Error(
                instance,
                var,
                val,
                self,
                "Variable must have a value assigned to it"
            )


class AutoIncrement( Mod ):
    type = "AutoIncrement"


class Unique( Mod ):
    type = "Unique"


class ForeignKey( Mod ):
    type = "ForeignKey"

    def __init__( self, namespace ):
        self.namespace = namespace


class Min( Mod ):
    type = "Min"

    class Min_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
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
    type = "Max"

    class Max_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
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
    type = "Length"

    class Length_Error( ValidationError ): pass

    def __init__( self, value ):
        self.value = value

    def validate( self, instance, var, val ):
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
    type = "InEnum"

    class InEnum_Error( ValidationError ): pass

    def __init__( self, values ):
        self.values = values

    def validate( self, instance, var, val ):
        if val is None: return
        if val not in self.values:
            raise InEnum.InEnum_Error(
                instance,
                var,
                val,
                self,
                "Value %s is not in enum" % var
            )
