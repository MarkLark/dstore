from nose.tools import ok_, eq_, raises, assert_raises
from . import BaseTest, Car, AllVars, Model, var, mod


class Validation( BaseTest ):
    def test_not_null( self ):
        with assert_raises( mod.NotNull.NotNull_Error ):
            Car( manufacturer = "Holden", year = 2000 ).add()

    def test_min( self ):
        with assert_raises( mod.Min.Min_Error ):
            Car( manufacturer = "Holden", make = "Commodore", year = 1901 ).add()

    def test_max( self ):
        with assert_raises( mod.Max.Max_Error ):
            Car( manufacturer = "Holden", make = "Commodore", year = 2105 ).add()

    def test_length( self ):
        with assert_raises( mod.Length.Length_Error ):
            Car( manufacturer = "Holden", make = "Commodore1Commodore1Commodore1Commodore1", year = 2005 ).add()

    def test_in_enum( self ):
        with assert_raises( mod.InEnum.InEnum_Error ):
            AllVars( string = "1234", enum = "five", cars_make_id = 0 ).add()

        AllVars(string="1234", enum="two", cars_make_id=0).add()

    def test_nulls( self ):
        AllVars( string = "1234", cars_make_id = 0 ).add()
