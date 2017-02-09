from . import BaseTest, Car
from dstore import Event


class EmptyAll( BaseTest ):
    def before_empty_all( self, event, store ):
        self.before = True

    def after_empty_all( self, event, store ):
        self.after = True

    def before_add( self, event, model, instance ):
        pass

    def after_add(self, event, model, instance):
        pass


    def test_print_store( self ):
        self.store.events.before_empty_all += self.before_empty_all
        self.store.events.after_empty_all  += self.after_empty_all

        print()
        self.store.events.print_table()

    def test_print_all( self ):
        self.store.events.before_empty_all += self.before_empty_all
        self.store.events.after_empty_all += self.after_empty_all
        Car.events.before_add += self.before_add
        Car.events.after_add += self.after_add

        print()
        Event.Manager.print_tables( [ self.store.events, Car.events ] )
