from .Error import EventNotFound, EventListenerNotFound, EventManagerNotReady


class Cancel( Exception ): pass


class Manager( object ):
    _events = []

    def __init__( self ):
        self.name   = None
        self._ready = False

    def init( self, name ):
        self.name   = name
        self.clear()
        self._ready = True

    def __getattr__( self, name ):
        if not self._ready: raise EventManagerNotReady( self )
        if name not in self._events: raise EventNotFound( self, name )
        if name not in self.__dict__: self.__dict__[ name ] = Event( self, name )
        return self.__dict__[ name ]

    def clear( self ):
        for name, event in self.__dict__.items():
            if not isinstance( event, Event ): continue
            event.listeners = []

    def print_table( self ):
        from tabulate import tabulate
        rows = []
        keys = [ "Event", "Listener" ]

        for name, event in self.__dict__.items():
            if not isinstance( event, Event ): continue
            for l in event.listeners:
                rows.append([
                    event.name,
                    "%s.%s" % ( l.__module__, l.__name__ )
                ])

        print tabulate(
            rows,
            headers = keys,
            tablefmt = "fancy_grid"
        )

    @staticmethod
    def print_tables( events ):
        from tabulate import tabulate
        rows = []
        keys = [ "Manager", "Event", "Listener" ]

        for mgr in events:
            if not isinstance( mgr, Manager ): continue
            for name, event in mgr.__dict__.items():
                if not isinstance( event, Event ): continue
                for l in event.listeners:
                    rows.append([
                        mgr.name,
                        event.name,
                        "%s.%s" % (l.__module__, l.__name__)
                    ])

        print tabulate(
            rows,
            headers = keys,
            tablefmt = "fancy_grid"
        )


class Event( object ):
    def __init__( self, mgr, name ):
        self.mgr       = mgr
        self.name      = name
        self.listeners = []

    def __iadd__( self, func ):
        self.listeners.append( func )
        return self

    def __isub__( self, func ):
        try:
            self.listeners.remove( func )
        except ValueError:
            raise EventListenerNotFound( self, func )
        return self

    def __call__( self, callee, **kwargs ):
        result = Result( self, callee, **kwargs )
        try:
            for l in self.listeners:
                l( result, **kwargs )
        except Cancel:
            pass
        return result


class Result( object ):
    def __init__( self, event, callee, **kwargs ):
        self.event  = event
        self.callee = callee
        self.args   = dict( **kwargs )
        self.result = True
        self.rtn    = dict()

    def cancel( self ):
        self.result = False
        raise Cancel()
