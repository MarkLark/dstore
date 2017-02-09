from nose.tools import eq_
from . import BaseTest, Car


class MemoryStore( BaseTest ):
    def test_fix_all_ids( self ):
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add().id = 25
        Car( manufacturer = "Holden", make = "Commodore", year = 2006 ).add().id = 40
        Car( manufacturer = "Holden", make = "Commodore", year = 2007 ).add().id = 33
        Car( manufacturer = "Holden", make = "Commodore", year = 2008 ).add().id = 105
        Car( manufacturer = "Holden", make = "Commodore", year = 2009 ).add().id = 69

        Car._store._fix_all_ids( Car._namespace )

        i = 0
        for car in Car.all():
            eq_( car.id, i, "Instance ID should be %d not %s" % ( i, car.id ) )
            i += 1
