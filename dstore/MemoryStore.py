from . import Store
from .Error import InstanceNotFound


class MemoryStore( Store ):
    def __init__( self, models = None, name = "DataStore", config = None, config_prefix = "DSTORE_", con_cache = None ):
        super( MemoryStore, self ).__init__( models, name, config, config_prefix, con_cache )
        self.data = {}

    def add( self, instance ):
        super( MemoryStore, self ).add( instance )
        self.data[ instance._namespace ].append( instance )
        instance.id = len( self.data[ instance._namespace ] ) - 1

    def delete( self, instance ):
        super( MemoryStore, self ).delete( instance )
        del self.data[ instance._namespace ][ instance.id ]
        self._fix_ids( instance )

    def update( self, instance ):
        super( MemoryStore, self ).update( instance )
        self.data[ instance._namespace ][ instance.id ].set( instance )

    def all( self, cls ):
        super( MemoryStore, self ).all( cls )
        return list( self.data[ cls._namespace ])

    def get( self, cls, row_id ):
        super( MemoryStore, self ).get( cls, row_id )
        try:
            return self.data[ cls._namespace ][ row_id ]
        except IndexError:
            raise InstanceNotFound( self, cls( id = row_id ) )

    def empty( self, cls ):
        super( MemoryStore, self ).empty( cls )
        self.data[ cls._namespace ] = []

    def create( self, cls ):
        super( MemoryStore, self ).create( cls )
        self.data[ cls._namespace ] = []

    def destroy( self, cls ):
        super( MemoryStore, self ).destroy( cls )
        self.data.pop( cls._namespace )

    def filter( self, cls, **kwargs ):
        super( MemoryStore, self ).filter( cls, **kwargs )
        rtn = []
        for row in self.data[ cls._namespace ]:
            add_row = True
            for var in cls._vars:
                if var.name not in kwargs: continue
                if kwargs[ var.name ] is None: continue

                if row.__dict__[ var.name ] != kwargs[ var.name ]:
                    add_row = False
                    break
            if add_row: rtn.append( row )

        num_rows = len( rtn )
        if num_rows == 0:
            kwargs[ "id" ] = -1
            raise InstanceNotFound( self, cls( **kwargs ) )

        return rtn

    def _fix_ids( self, instance ):
        i = instance.id
        for row in self.data[ instance._namespace ][ i: ]:
            row.id = i
            i += 1

    def _fix_all_ids( self, namespace ):
        i = 0
        for row in self.data[ namespace ]:
            row.id = i
            i += 1
