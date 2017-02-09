from nose.tools import raises
from . import BaseTest, Car, AllVars, mod


class Validation( BaseTest ):
    @raises( mod.NotNull.NotNull_Error )
    def test_not_null( self ):
        Car( manufacturer = "Holden", year = 2000 ).add()

    @raises( mod.Min.Min_Error )
    def test_min( self ):
        Car( manufacturer = "Holden", make = "Commodore", year = 1901 ).add()

    @raises( mod.Max.Max_Error )
    def test_max( self ):
        Car( manufacturer = "Holden", make = "Commodore", year = 2105 ).add()

    @raises( mod.Length.Length_Error )
    def test_length( self ):
        Car( manufacturer = "Holden", make = "Commodore1Commodore1Commodore1Commodore1", year = 2005 ).add()

    @raises( mod.InEnum.InEnum_Error )
    def test_in_enum( self ):
        AllVars( string = "1234", enum = "five", cars_make_id = 0 ).add()

    def test_nulls( self ):
        AllVars( string = "1234", cars_make_id = 0 ).add()
