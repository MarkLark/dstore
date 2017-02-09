from .Error import ModelNotRegistered, ModelNotFound
from . import Event
from .Model import ModelEvents


class StoreEvents( Event.Manager ):
    _events = [
        "before_init_app", "after_init_app",
        "before_destroy_app", "after_destroy_app",
        "before_register_models", "after_register_models",
        "before_register_model", "after_register_model",
        "before_create_all", "after_create_all",
        "before_destroy_all", "after_destroy_all",
        "before_empty_all", "after_empty_all",
        "before_connect", "after_connect",
        "before_disconnect", "after_disconnect",
        "before_add_bulk", "after_add_bulk"
    ]

    def __getattr__( self, name ):
        if not name == "before_init_app" or self._ready: return super( StoreEvents, self ).__getattr__( name )

        self._ready = True
        rtn = super( StoreEvents, self ).__getattr__( name )
        self._ready = False
        return rtn


class Store( object ):
    def __init__( self, models = None, name = "DataStore", config = None, config_prefix = "DSTORE_", con_cache = None ):
        self.config = {}
        self.config_prefix = config_prefix
        self.name    = name
        self.models  = list( models ) or []
        self.con_cache = con_cache
        self._con = None

        if config is not None: self.set_config( config )

        self.events = StoreEvents()

    def set_config_defaults( self, opts ):
        for key, val in opts.items(): self.config.setdefault( key, val )

    def set_config( self, opts ):
        for key, val in opts.items():
            if not key.startswith( self.config_prefix ): continue
            self.config[ key ] = val

    def get_config( self, key ):
        return self.config[ key ]

    def get_configs( self, remove_prefix = True, to_lower = True, prefix = None ):
        rtn = {}
        if prefix is None: prefix = self.config_prefix
        prefix_len = len( prefix )
        for key, val in self.config.items():
            if key.startswith( prefix ):
                if remove_prefix: key = key[ prefix_len: ]
                if to_lower: key      = key.lower()
                rtn[ key ] = val
        return rtn

    def init_app( self ):
        self.init_event_managers()
        self.events.before_init_app( self, store = self )
        self.register_models()
        self.events.after_init_app( self, store = self )

    def destroy_app( self ):
        self.events.before_destroy_app( self, store = self )
        self.events.after_destroy_app( self, store = self )

    def connect( self ):
        self.events.before_connect( self, store = self )
        self.events.after_connect( self, store = self )
        return self

    def disconnect( self ):
        self.events.before_disconnect( self, store = self )
        self._con = None
        self.events.after_disconnect( self, store = self )

    @property
    def con( self ):
        if self.con_cache is not None:
            con = self.con_cache( self )
        else:
            if self._con is None: self._con = self.connect()
            con = self._con
        return con

    def init_event_managers( self ):
        listeners = self.events.before_init_app.listeners
        self.events.init( self.name )
        self.events.before_init_app.listeners = listeners

        for model in self.models:
            model.events = ModelEvents()
            model.events.init( model._namespace )

    def register_models( self ):
        self.events.before_register_models( self, store = self )
        for model in self.models:
            self.events.before_register_model( self, store = self, model = model )
            self.register_model( model )
            self.events.after_register_model( self, store = self, model = model )
        self.events.after_register_models( self, store = self )

    def register_model( self, model ):
        model._store       = self

    def add( self, instance ):
        if instance.__class__ not in self.models: raise ModelNotRegistered( self, instance.__class__ )

    def delete( self, instance ):
        if instance.__class__ not in self.models: raise ModelNotRegistered( self, instance.__class__ )

    def update( self, instance ):
        if instance.__class__ not in self.models: raise ModelNotRegistered( self, instance.__class__ )

    def all( self, cls ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def get( self, cls, row_id ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def empty( self, cls ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def create( self, cls ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def destroy( self, cls ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def filter( self, cls, **kwargs ):
        if cls not in self.models: raise ModelNotRegistered( self, cls )

    def create_all( self ):
        self.events.before_create_all( self, store = self )
        for model in self.models:
            model.create()
        self.events.after_create_all( self, store = self )

    def destroy_all( self ):
        self.events.before_destroy_all( self, store = self )
        for model in reversed( self.models ):
            model.destroy()
        self.events.after_destroy_all( self, store = self )

    def empty_all( self ):
        self.events.before_empty_all( self, store = self )
        for model in reversed( self.models ):
            model.empty()
        self.events.after_empty_all( self, store = self )

    def get_model( self, namespace ):
        for model in self.models:
            if model._namespace == namespace: return model
        raise ModelNotFound( self, namespace )

    def add_bulk( self, data = None ):
        self.events.before_add_bulk( self, store = self, data = data )
        for namespace in data:
            try:
                model = self.get_model( namespace )
            except ModelNotFound:
                continue

            for row in data[namespace]:
                model( **row ).add()
        self.events.after_add_bulk( self, store = self, data = data )
