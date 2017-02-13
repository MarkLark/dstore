from . import Store
from .Error import InstanceNotFound


class MemoryStore( Store ):
    def __init__( self, models = None, name = "DataStore", config = None, config_prefix = "DSTORE_", con_cache = None ):
        super( MemoryStore, self ).__init__( models, name, config, config_prefix, con_cache )
        self.data    = {}
        self.next_id = {}

    def add( self, instance ):
        super( MemoryStore, self ).add( instance )
        instance.id = self.next_id[ instance._namespace ]
        self.data[ instance._namespace ][ instance.id ] = instance
        self.next_id[ instance._namespace ] += 1

    def delete( self, instance ):
        super( MemoryStore, self ).delete( instance )
        self.data[ instance._namespace ].pop( instance.id )

    def update( self, instance ):
        super( MemoryStore, self ).update( instance )
        self.data[ instance._namespace ][ instance.id ].set( instance )

    def all( self, cls ):
        super( MemoryStore, self ).all( cls )
        return list( self.data[ cls._namespace ].values() )

    def get( self, cls, row_id ):
        super( MemoryStore, self ).get( cls, row_id )
        try:
            return self.data[ cls._namespace ][ row_id ]
        except KeyError:
            raise InstanceNotFound( self, cls( id = row_id ) )

    def empty( self, cls ):
        super( MemoryStore, self ).empty( cls )
        self.data[ cls._namespace ] = {}

    def create( self, cls ):
        super( MemoryStore, self ).create( cls )
        self.data[ cls._namespace ] = {}
        self.next_id[ cls._namespace ] = 0

    def destroy( self, cls ):
        super( MemoryStore, self ).destroy( cls )
        self.data.pop( cls._namespace )
        self.next_id[ cls._namespace ] = 0

    def filter( self, cls, **kwargs ):
        super( MemoryStore, self ).filter( cls, **kwargs )
        rtn = []
        for row in self.data[ cls._namespace ].values():
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
