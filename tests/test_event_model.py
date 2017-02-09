from nose.tools import eq_, raises
from . import BaseTest, Car
from dstore.Error import InstanceNotFound


class CancelAdd( BaseTest ):
    def before_addd( self, event, model, instance ):
        self.action = True
        event.cancel()

    @raises( InstanceNotFound )
    def test( self ):
        Car.events.before_add += self.before_addd
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car.events.before_add -= self.before_addd

        Car.get( 0 )

        eq_( self.action, True, "before_add was not executed" )


class Add( BaseTest ):
    def before_action( self, event, model, instance ):
        self.before = ( model, instance )

    def after_action( self, event, model, instance ):
        self.after = ( model, instance )

    def test(self):
        Car.events.before_add += self.before_action
        Car.events.after_add += self.after_action

        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()

        eq_( issubclass( self.before[0], Car ), True, "before_add was not executed (Model != Car)")
        eq_( isinstance( self.before[1], Car ), True, "before_add was not executed (Instance not a Car)")
        eq_( issubclass( self.after[0], Car ), True, "after_add was not executed (Model != Car)")
        eq_( isinstance( self.after[1], Car ), True, "after_add was not executed (Instance not a Car)")


class Delete( BaseTest ):
    def before_action( self, event, model, instance ):
        self.before = ( model, instance )

    def after_action( self, event, model, instance ):
        self.after = ( model, instance )

    def test(self):
        Car.events.before_delete += self.before_action
        Car.events.after_delete  += self.after_action

        car = Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        car.delete()

        eq_( issubclass( self.before[0], Car ), True, "before_delete was not executed (Model != Car)")
        eq_( isinstance( self.before[1], Car ), True, "before_delete was not executed (Instance not a Car)")
        eq_( issubclass( self.after[0], Car ), True, "after_delete was not executed (Model != Car)")
        eq_( isinstance( self.after[1], Car ), True, "after_delete was not executed (Instance not a Car)")


class Update( BaseTest ):
    def before_action( self, event, model, instance ):
        self.before = ( model, instance )

    def after_action( self, event, model, instance ):
        self.after = ( model, instance )

    def test(self):
        Car.events.before_update += self.before_action
        Car.events.after_update  += self.after_action

        car = Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        car.year = 2016
        car.update()

        eq_( issubclass( self.before[0], Car ), True, "before_update was not executed (Model != Car)")
        eq_( isinstance( self.before[1], Car ), True, "before_update was not executed (Instance not a Car)")
        eq_( issubclass( self.after[0], Car ), True, "after_update was not executed (Model != Car)")
        eq_( isinstance( self.after[1], Car ), True, "after_update was not executed (Instance not a Car)")


class All( BaseTest ):
    def before_action( self, event, model ):
        self.before = model

    def after_action( self, event, model, instances ):
        self.after = ( model, instances )

    def test( self ):
        Car.events.before_all += self.before_action
        Car.events.after_all += self.after_action

        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2006 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2007 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2008 ).add()

        Car.all()

        eq_( issubclass( self.before, Car ), True, "before_all was not executed (Model != Car)" )
        eq_( issubclass( self.after[0], Car ), True, "after_all was not execute (Model != Car)" )
        eq_( isinstance( self.after[1], list ), True, "after_all was not execute (Instance != List)" )
        eq_( isinstance( self.after[1][0], Car), True, "after_all was not execute (Instance[0] != Car)" )


class Get( BaseTest ):
    def before_action( self, event, model, row_id ):
        self.before = ( model, row_id )

    def after_action( self, event, model, instance ):
        self.after = ( model, instance )

    def test( self ):
        Car.events.before_get += self.before_action
        Car.events.after_get += self.after_action

        Car(manufacturer="Holden", make="Commodore", year=2005).add()
        Car(manufacturer="Holden", make="Commodore", year=2006).add()

        Car.get( 1 )

        eq_( issubclass( self.before[0], Car ), True, "before_get was not execute (Model != Car)" )
        eq_( self.before[1], 1, "before_get was not execute (row_id != 1)" )
        eq_( issubclass( self.after[0], Car ), True, "after_get was not executed (Model != Car)" )
        eq_( isinstance( self.after[1], Car ), True, "after_get was not execute (Instance != Car)" )
        eq_( self.after[1].year, 2006, "after_get was not execute (Instance.year != 2006)" )


class Empty( BaseTest ):
    def before_action( self, event, model ):
        self.before = model

    def after_action( self, event, model ):
        self.after = model

    def test( self ):
        Car.events.before_empty += self.before_action
        Car.events.after_empty += self.after_action

        Car(manufacturer="Holden", make="Commodore", year=2005).add()
        Car(manufacturer="Holden", make="Commodore", year=2006).add()

        Car.empty()

        eq_( issubclass( self.before, Car ), True, "before_empty was not executed (Model != Car)" )
        eq_( issubclass( self.after, Car ), True, "after_empty was not execute (Model != Car)" )


class Create( BaseTest ):
    auto_create = False

    def before_action( self, event, model ):
        self.before = model

    def after_action( self, event, model ):
        self.after = model

    def test( self ):
        Car.events.before_create += self.before_action
        Car.events.after_create += self.after_action

        Car.create()
        Car.destroy()

        eq_( issubclass( self.before, Car), True, "before_create was not execute (Model != Car)" )
        eq_( issubclass( self.after, Car ), True, "after_create was not execute (Model != Car" )


class Destroy( BaseTest ):
    auto_create = False

    def before_action( self, event, model ):
        self.before = model

    def after_action( self, event, model ):
        self.after = model

    def test( self ):
        Car.events.before_destroy += self.before_action
        Car.events.after_destroy += self.after_action

        Car.create()
        Car.destroy()

        eq_( issubclass( self.before, Car ), True, "before_destroy was not execute (Model != Car)" )
        eq_( issubclass( self.after, Car ), True, "after_destroy was not execute (Model != Car" )


class Filter( BaseTest ):
    def before_action( self, event, model, params ):
        self.before = ( model, params )

    def after_action( self, event, model, instances, params ):
        self.after = ( model, instances, params )

    def test( self ):
        Car.events.before_filter += self.before_action
        Car.events.after_filter += self.after_action

        Car(manufacturer="Holden", make="Commodore", year=2005).add()
        Car(manufacturer="Holden", make="Commodore", year=2006).add()
        Car(manufacturer="Holden", make="Rodeo", year=2007).add()
        Car(manufacturer="Holden", make="Colorado", year=2008).add()

        cars = Car.filter( make = "Commodore" )

        eq_( issubclass( self.before[0], Car ), True, "before_filter was not executed (Model != Car)" )
        eq_( isinstance( self.before[1], dict ), True, "before_filter was not executed (Params != Dict)" )
        eq_( self.before[1][ "make" ], "Commodore", "before_filter was not executed (Params['make'] != 'Commodore'" )
        eq_( issubclass( self.after[0], Car ), True, "after_filter was not executed (Model != Car)" )
        eq_( isinstance( self.after[1], list ), True, "after_filter was not executed (Instances != List)" )
        eq_( isinstance( self.after[1][0], Car ), True, "after_filter was not executed (Instances[0] != Car)" )
        eq_( isinstance( self.after[2], dict ), True, "after_filter was not executed (Params != Dict)" )
        eq_( self.after[2][ "make" ], "Commodore", "after_filter was not executed (Params['make'] != 'Commodore'" )


class Validate( BaseTest ):
    def before_action( self, event, model, instance ):
        self.before = ( model, instance )

    def after_action( self, event, model, instance ):
        self.after = ( model, instance )

    def test( self ):
        Car.events.before_validate += self.before_action
        Car.events.after_validate += self.after_action

        Car(manufacturer="Holden", make="Commodore", year=2005).add()

        eq_( issubclass( self.before[0], Car ), True, "before_validate was not executed (Model != Car)" )
        eq_( isinstance( self.before[1], Car ), True, "before_validate was not executed (Instance != Car)" )
        eq_( issubclass( self.after[0], Car ), True, "after_validate was not executed (Model != Car)" )
        eq_( isinstance( self.after[1], Car ), True, "after_validate was not executed (Instance != Car)" )
