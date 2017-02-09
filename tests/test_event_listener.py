from nose.tools import eq_, raises
from dstore import MemoryStore
from dstore.Error import EventNotFound, EventListenerNotFound, EventManagerNotReady
from . import BaseTest


class UnknownEvent( BaseTest ):
    auto_create = False
    auto_init   = False

    @raises( EventNotFound )
    def test( self ):
        store = MemoryStore( self.models )
        store.init_app()
        store.events.before_something += self.test


class UnknownListener( BaseTest ):
    auto_create = False
    auto_init   = False

    @raises( EventListenerNotFound )
    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_init_app -= self.test


class AddListener( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_init_app( self, event, store ):
        self.action = True

    def test( self ):
        self.action = False
        store = MemoryStore( self.models )
        store.events.before_init_app += self.before_init_app

        store.init_app()
        eq_( self.action, True, "before_init_app was not executed" )


class RemoveListener( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_init_app( self, event, store ):
        self.action = True

    def test( self ):
        self.action = False
        store = MemoryStore( self.models )

        store.events.before_init_app += self.before_init_app
        store.events.before_init_app -= self.before_init_app

        store.init_app()
        eq_( self.action, False, "before_init_app was executed" )


class ManagerNotReady( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_register_models( self, event, store ):
        pass

    @raises( EventManagerNotReady )
    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_register_models += self.before_register_models
