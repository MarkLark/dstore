from nose.tools import ok_, eq_, raises, assert_raises
from . import BaseTest, Car, AllVars, Model, var, mod


class Store( BaseTest ):
    auto_create = False

    def test_create_destroy( self ):
        Car.create()
        Car.destroy()

    def test_empty_all( self ):
        self.store.create_all()
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        self.store.empty_all()
        self.store.destroy_all()

    def test_get_con( self ):
        con = self.store.con

    def test_get_con_cache( self ):
        self.store.con_cache = con_cache
        con = self.store.con


def con_cache( store ):
    return store
