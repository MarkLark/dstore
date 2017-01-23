from nose.tools import eq_
from dstore import MemoryStore, Model
from . import BaseTest, Car


class Init( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_init_app( self, event, store ):
        store.events.after_init_app += self.after_init_app
        self.before = True

    def after_init_app( self, event, store ):
        self.after = True

    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_init_app += self.before_init_app
        store.init_app()

        eq_( self.before, True, "before_init_app was not executed" )
        eq_( self.after,  True, "after_init_app was not executed"  )


class Destroy( BaseTest ):
    auto_create = False
    auto_init = False

    def before_init_app( self, event, store ):
        store.events.after_destroy_app += self.after_destroy_app
        self.before = True

    def after_destroy_app( self, event, store ):
        self.after = True

    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_init_app += self.before_init_app
        store.init_app()
        store.destroy_app()

        eq_( self.before, True, "before_destroy_app was not executed" )
        eq_( self.after,  True, "after_destroy_app was not executed"  )


class RegisterModels( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_init_app( self, event, store ):
        store.events.before_register_models += self.before_register_models
        store.events.after_register_models  += self.after_register_models

    def before_register_models( self, event, store ):
        self.before = True

    def after_register_models( self, event, store ):
        self.after = True

    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_init_app += self.before_init_app

        store.init_app()
        store.destroy_app()

        eq_( self.before, True, "before_register_models was not executed" )
        eq_( self.after,  True, "after_register_models was not executed"  )


class RegisterModel( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_init_app( self, event, store ):
        store.events.before_register_model += self.before_register_model
        store.events.after_register_model  += self.after_register_model

    def before_register_model( self, event, store, model ):
        self.before = model

    def after_register_model( self, event, store, model ):
        self.after = model

    def test(self):
        store = MemoryStore(self.models)
        store.events.before_init_app += self.before_init_app

        store.init_app()
        store.destroy_app()

        eq_( issubclass( self.before, Model ), True, "before_register_model was not executed" )
        eq_( issubclass( self.after,  Model ), True, "after_register_model was not executed"  )


class Connect( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_action( self, event, store ):
        self.before = store

    def after_action( self, event, store ):
        self.after = store

    def test( self ):
        store = MemoryStore(self.models)
        store.events.before_connect = self.before_action
        store.events.after_connect = self.after_action

        store.init_app()
        store.connect()

        eq_( self.before, store, "before_connect was not executed" )
        eq_( self.after,  store, "after_connect was not executed"  )


class Disconnect( BaseTest ):
    auto_create = False
    auto_init   = False

    def before_action( self, event, store ):
        self.before = store

    def after_action( self, event, store ):
        self.after = store

    def test( self ):
        store = MemoryStore( self.models )
        store.events.before_disconnect = self.before_action
        store.events.after_disconnect = self.after_action

        store.init_app()
        store.connect()
        store.disconnect()

        eq_( self.before, store, "before_disconnect was not executed" )
        eq_( self.after,  store, "after_disconnect was not executed"  )


class CreateAll( BaseTest ):
    auto_create = False

    def before_create_all( self, event, store ):
        self.before = True

    def after_create_all( self, event, store ):
        self.after = True

    def test( self ):
        self.store.events.before_create_all += self.before_create_all
        self.store.events.after_create_all  += self.after_create_all

        self.store.create_all()

        eq_( self.before, True, "before_create_all was not executed" )
        eq_( self.after,  True, "after_create_all was not executed"  )


class DestroyAll( BaseTest ):
    auto_create = False

    def before_destroy_all( self, event, store ):
        self.before = True

    def after_destroy_all( self, event, store ):
        self.after = True

    def test( self ):
        self.store.events.before_destroy_all += self.before_destroy_all
        self.store.events.after_destroy_all  += self.after_destroy_all

        self.store.create_all()
        self.store.destroy_all()

        eq_( self.before, True, "before_destroy_all was not executed" )
        eq_( self.after,  True, "after_destroy_all was not executed"  )


class EmptyAll( BaseTest ):
    def before_empty_all( self, event, store ):
        self.before = True

    def after_empty_all( self, event, store ):
        self.after = True

    def test( self ):
        self.store.events.before_empty_all += self.before_empty_all
        self.store.events.after_empty_all  += self.after_empty_all

        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2006 ).add()

        self.store.empty_all()

        eq_( self.before, True, "before_empty_all was not executed" )
        eq_( self.after,  True, "after_empty_all was not executed"  )

        cars = Car.all()

        num_cars = len( cars )
        eq_( num_cars, 0, "Number of cars should be 0 not %d" % num_cars )
