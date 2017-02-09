from nose.tools import eq_
from . import BaseTest, Car


class Bulk( BaseTest ):
    def test_add_json( self ):
        data = {
            "cars.make": [
                { "manufacturer": "Holden", "make": "Commodore", "year": 2005 },
                { "manufacturer": "Holden", "make": "Commodore", "year": 2006 },
                { "manufacturer": "Holden", "make": "Commodore", "year": 2007 },
                { "manufacturer": "Holden", "make": "Commodore", "year": 2008 },
            ],
            "doesnt.exist": [
                { "some": "new", "data": "not", "to": "fail" }
            ]
        }
        self.store.add_bulk( data )

        oid = 0
        year = 2005
        for car in Car.all():
            eq_(car.id, oid, "Instance ID should be %d not %d" % (oid, car.id) )
            eq_(car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer)
            eq_(car.make, "Commodore", "Instance Make should be 'Commodore' not '%s'" % car.make)
            eq_(car.year, year, "Instance Year should be %d not %d" % (year, car.year) )
            oid  += 1
            year += 1
