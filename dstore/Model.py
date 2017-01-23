from .Error import IncompatibleSource
from . import Event


class ModelEvents( Event.Manager ):
    _events = [
        "before_add", "after_add",
        "before_delete", "after_delete",
        "before_update", "after_update",
        "before_validate", "after_validate",
        "before_all", "after_all",
        "before_get", "after_get",
        "before_empty", "after_empty",
        "before_create", "after_create",
        "before_destroy", "after_destroy",
        "before_filter", "after_filter"
    ]


class Model( object ):
    _namespace = None
    _vars      = []
    _store     = None
    events     = ModelEvents()

    @classmethod
    def get_var( cls, name, typename = None ):
        for var in cls._vars:
            if var.name == name:
                if typename is None: return var
                elif var.type == typename: return var
        return None

    def __init__( self, **kwargs ):
        self.set( kwargs )

    def __repr__( self ):
        rtn = "%s(" % self._namespace
        for var in self._vars:
            rtn += "%s = '%s', " % ( var.name, self.__dict__[ var.name ] )

        rtn = rtn[ :-2 ]
        rtn += ")"
        return rtn

    def to_dict( self, include_null = False ):
        rtn = {}
        for var in self._vars:
            val = self.__dict__[ var.name ]
            if val is None and not include_null: continue
            rtn[ var.name ] = val
        return rtn

    def set( self, other ):
        if isinstance( other, Model ):
            if not isinstance( other, self.__class__ ): raise IncompatibleSource( self._store, self, other )
            other = other.__dict__
        elif not isinstance( other, dict ): raise IncompatibleSource( self._store, self, other )

        for var in self._vars: self._set_var( var, other )

    def _set_var( self, var, other ):
        if var.name == "id" and "id" in self.__dict__: return
        elif var.name not in other or other[ var.name ] is None:
            if var.name in self.__dict__ and self.__dict__[ var.name ] is not None: return
            val = var.default
        else:
            val = other[ var.name ]

        self.__dict__[ var.name ] = val

    def add( self ):
        rtn = self.events.before_add( self, model = self.__class__, instance = self )
        if rtn.result is False: return rtn

        self.validate()
        self._store.add( self )
        self.events.after_add( self, model = self.__class__, instance = self )
        return self

    def delete( self ):
        self.events.before_delete( self, model = self.__class__, instance = self )
        self._store.delete( self )
        self.events.after_delete( self, model = self.__class__, instance = self )

    def update( self ):
        self.events.before_update( self, model = self.__class__, instance = self )
        self._store.update( self )
        self.events.after_update( self, model = self.__class__, instance = self )

    def validate( self ):
        self.events.before_validate( self, model = self.__class__, instance = self )
        for var in self._vars: var.validate( self )
        self.events.after_validate( self, model = self.__class__, instance = self )

    @classmethod
    def all( cls, to_dict = False ):
        cls.events.before_all( cls, model = cls )
        instances = cls._store.all( cls )
        if to_dict:
            rtn = []
            for instance in instances:
                rtn.append( instance.to_dict() )
            instances = rtn
        cls.events.after_all( cls, model = cls, instances = instances )
        return instances

    @classmethod
    def get( cls, row_id ):
        cls.events.before_get( cls, model = cls, row_id = row_id )
        instance = cls._store.get( cls, row_id )
        cls.events.after_get( cls, model = cls, instance = instance )
        return instance

    @classmethod
    def empty( cls ):
        cls.events.before_empty( cls, model = cls )
        cls._store.empty( cls )
        cls.events.after_empty( cls, model = cls )

    @classmethod
    def create( cls ):
        cls.events.before_create( cls, model = cls )
        cls._store.create( cls )
        cls.events.after_create( cls, model = cls )

    @classmethod
    def destroy( cls ):
        cls.events.before_destroy( cls, model = cls )
        cls._store.destroy( cls )
        cls.events.after_destroy( cls, model = cls )

    @classmethod
    def filter( cls, **kwargs ):
        cls.events.before_filter( cls, model = cls, params = kwargs )
        instances = cls._store.filter( cls, **kwargs )
        cls.events.after_filter( cls, model = cls, instances = instances, params = kwargs )
        return instances

    @classmethod
    def print_table( cls ):
        from tabulate import tabulate
        rows = cls.all()

        keys = [ ]
        for col in cls._vars:
            keys.append( str( col.name ) )
        values = [ ]

        if len( rows ) == 0:
            print "<- EMPTY ->"
            return

        for row in rows:
            v = [ ]
            for key in keys:
                v.append( str( row.__dict__[ key ] ) )
            values.append( v )

        print tabulate(
            values,
            headers = keys,
            tablefmt = "fancy_grid"
        )

