from nose.tools import ok_, eq_, raises, assert_raises
from . import BaseTest, Car, AllVars, Model, var, mod


class Convert( BaseTest ):
    def test_print_table( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        Car.print_table()

    def test_print_empty_table( self ):
        Car.print_table()

    def test_all_to_dict( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        cars = Car.all( to_dict = True )

        num_cars = len( cars )
        eq_( num_cars, 6, "Number of cars should be 6 not %d" % num_cars )

        rtn = [
            { "id": 0, "manufacturer": "Holden", "make": "Rodeo",     "year": 2002 },
            { "id": 1, "manufacturer": "Holden", "make": "Commodore", "year": 2003 },
            { "id": 2, "manufacturer": "Holden", "make": "Commodore", "year": 2004 },
            { "id": 3, "manufacturer": "Holden", "make": "Commodore", "year": 2005 },
            { "id": 4, "manufacturer": "Holden", "make": "Colorado",  "year": 2006 },
            { "id": 5, "manufacturer": "Ford",   "make": "Falcon",    "year": 2007 }
        ]

        eq_( cars, rtn, "Dictionary of Cars does not match the expected output" )

    def test_to_string( self ):
        Car( manufacturer = "Holden", make = "Rodeo", year = 2002 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2003 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2004 ).add()
        Car( manufacturer = "Holden", make = "Commodore", year = 2005 ).add()
        Car( manufacturer = "Holden", make = "Colorado", year = 2006 ).add()
        Car( manufacturer = "Ford", make = "Falcon", year = 2007 ).add()

        for car in Car.all():
            print( car )

    def test_to_dict_with_none( self ):
        print( Car( manufacturer = "Holden", make = "Rodeo" ).to_dict() )
