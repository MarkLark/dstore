from nose.tools import ok_, eq_, raises, assert_raises
from . import BaseTest, Car, AllVars, Model, var, mod


class CRUD( BaseTest ):
    def test_add_single( self ):
        car = Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()

        eq_( car.id, 0, "Instance ID should be 0 not %d" % car.id )
        eq_( car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer )
        eq_( car.make, "Commodore", "Instance Make should be 'Commodore' not '%s'" % car.make )
        eq_( car.year, 2005, "Instance Year should be 2005 not %d" % car.year )

    def test_add_multiple( self ):
        cars = [
            Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add(),
            Car( manufacturer = "Holden", make = "Commodore", year = 2006 ).add(),
            Car( manufacturer = "Holden", make = "Commodore", year = 2007 ).add(),
            Car( manufacturer = "Holden", make = "Commodore", year = 2008 ).add(),
            Car( manufacturer = "Holden", make = "Commodore", year = 2009 ).add(),
            Car( manufacturer = "Holden", make = "Commodore", year = 2010 ).add()
        ]

        i = 0
        y = 2005
        for car in cars:
            eq_( car.id, i, "Instance ID should be %d not %d" % ( i, car.id ) )
            eq_( car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer )
            eq_( car.make, "Commodore", "Instance Make should be 'Commodore' not '%s'" % car.make )
            eq_( car.year, y, "Instance Year should be %d not %d" % ( y, car.year ) )
            i += 1
            y += 1

    def test_get( self ):
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        car = Car.get( 0 )

        eq_( car.id, 0, "Instance ID should be 0 not %d" % car.id )
        eq_( car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer )
        eq_( car.make, "Commodore", "Instance Make should be 'Commodore' not '%s'" % car.make )
        eq_( car.year, 2005, "Instance Year should be 2005 not %d" % car.year )

    def test_filter( self ):
        Car( manufacturer = "Holden", make = "Rodeo",     year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado" , year = 2006 ).add()
        Car( manufacturer = "Ford",   make = "Falcon",    year = 2007 ).add()

        cars = Car.filter( manufacturer = "Holden" )

        num_cars = len( cars )
        eq_( num_cars, 5, "Should have filtered out 5 Cars not %d" % num_cars )
        i = 0
        y = 2002
        for car in cars:
            eq_( car.id, i, "Instance ID should be %d not %d" % ( i, car.id ) )
            eq_( car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer )
            eq_( car.year, y, "Instance Year should be %d not %d" % (y, car.year) )
            i += 1
            y += 1

    def test_all( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        cars = Car.all()
        num_cars = len( cars )
        eq_( num_cars, 6, "Should have filtered out 6 Cars not %d" % num_cars )

        i = 0
        y = 2002
        for car in cars:
            eq_( car.id, i, "Instance ID should be %d not %d" % (i, car.id) )
            eq_( car.year, y, "Instance Year should be %d not %d" % (y, car.year) )
            i += 1
            y += 1

    def test_update( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()

        car = Car.get( 0 )
        car.year = 2016
        car.update()

        car = Car.get( 0 )
        eq_( car.year, 2016, "Instance Year should be 2016 not %d" % car.year )

    def test_delete( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        car = Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        car.delete()

    def test_delete_all( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        i = 6
        while i > 0:
            num_cars = len( Car.all() )
            eq_( num_cars, i, "Number of cars should be %d not %d" % ( i, num_cars ) )
            i -= 1
            Car.get( i ).delete()

    def test_empty( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        num_cars = len( Car.all() )
        eq_( num_cars, 6, "Number of cars should be 6 not %d" % num_cars )

        Car.empty()
        num_cars = len( Car.all() )
        eq_( num_cars, 0, "Number of cars should be 0 not %d" % num_cars )

    def test_filter_with_arg_none( self ):
        Car( manufacturer = "Holden", make = "Rodeo",     year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado" , year = 2006 ).add()
        Car( manufacturer = "Ford",   make = "Falcon",    year = 2007 ).add()

        cars = Car.filter( manufacturer = "Holden", year = None )

        num_cars = len( cars )
        eq_( num_cars, 5, "Should have filtered out 5 Cars not %d" % num_cars )
        i = 0
        y = 2002
        for car in cars:
            eq_( car.id, i, "Instance ID should be %d not %d" % ( i, car.id ) )
            eq_( car.manufacturer, "Holden", "Instance Manufacturer should be 'Holden' not '%s'" % car.manufacturer )
            eq_( car.year, y, "Instance Year should be %d not %d" % (y, car.year) )
            i += 1
            y += 1
