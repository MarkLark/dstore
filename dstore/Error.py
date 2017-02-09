class BaseError( Exception ): pass


class StoreError( BaseError ):
    def __init__( self, store, *args, **kwargs ):
        self.store = store
        super( StoreError, self ).__init__( *args, **kwargs )


class ModelError( StoreError ):
    def __init__( self, store, model, *args, **kwargs ):
        self.model = model
        super( ModelError, self ).__init__( store, *args, **kwargs )


class EventError( BaseError ):
    def __init__( self, mgr, event, *args, **kwargs ):
        self.mgr   = mgr
        self.event = event
        super( EventError, self ).__init__( *args, **kwargs )


class ModelNotRegistered( ModelError ):
    def __init__( self, store, model ):
        super( ModelNotRegistered, self ).__init__(
            store,
            model,
            "%s is not registered with %s" % ( model._namespace, store.name )
        )


class InstanceNotFound( ModelError ):
    def __init__( self, store, instance ):
        super( InstanceNotFound, self ).__init__(
            store,
            instance.__class__,
            "%s.%s[%d] does not exist" % ( store.name, instance._namespace, instance.id )
        )


class IncompatibleSource( ModelError ):
    def __init__( self, store, instance, other ):
        super( IncompatibleSource, self ).__init__(
            store,
            instance.__class__,
            "Cannot assign values from an incompatble source"
        )


class ValidationError( ValueError ):
    def __init__( self, instance, var, val, mod, message = "" ):
        self.instance = instance
        self.var = var
        self.val = val
        self.mod = mod

        msg = "%s[%d].%s = %s. %s: %s" % (
            instance._namespace,
            instance.id or -1,
            var.name,
            val,
            mod.type,
            message
        )

        super( ValidationError, self ).__init__( msg )


class EventNotFound( EventError ):
    def __init__( self, mgr, event ):
        super( EventNotFound, self ).__init__(
            mgr,
            event,
            "Event %s.%s not found" % (
                mgr.name,
                event
            )
        )


class EventListenerNotFound( EventError ):
    def __init__( self, event, func ):
        super( EventListenerNotFound, self ).__init__(
            event.mgr,
            event,
            "Listener not found in event %s.%s" % (
                event.mgr.name,
                event.name
            )
        )


class EventManagerNotReady( EventError ):
    def __init__( self, mgr ):
        super( EventManagerNotReady, self ).__init__(
            mgr,
            None,
            "EventManager for %s is not ready" % mgr.name
        )


class ModelNotFound( ModelError ):
    def __init__( self, store, namespace ):
        super( ModelNotFound, self ).__init__(
            store,
            namespace,
            "Model %s not found in store %s" % (namespace, store.name)
        )
