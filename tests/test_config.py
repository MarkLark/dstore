from nose.tools import ok_, eq_, raises, assert_raises
from . import BaseTest, Car, AllVars, Model, var, mod


class Config( BaseTest ):
    def test_set_defaults( self ):
        self.store.set_config_defaults({
            "DSTORE_TEST_1": 1,
            "DSTORE_TEST_2": 2,
            "DSTORE_TEST_3": 3,
            "DSTORE_TEST_4": 4,
        })

    def test_set( self ):
        self.store.set_config_defaults({
            "DSTORE_TEST_1": 1,
            "DSTORE_TEST_2": 2,
            "DSTORE_TEST_3": 3,
            "DSTORE_TEST_4": 4,
        })

        self.store.set_config({
            "DSTORE_TEST_1": 1,
            "DSTORE_TEST_2": 2,
            "DSTORE_TEST_4": 5,
            "SOMETHING_ELSE": False
        })

    def test_get( self ):
        self.store.set_config_defaults({
            "DSTORE_TEST_1": 1,
            "DSTORE_TEST_2": 2,
            "DSTORE_TEST_3": 3,
            "DSTORE_TEST_4": 4,
        })

        opt = self.store.get_config( "DSTORE_TEST_1" )

    def test_get_all( self ):
        self.store.set_config_defaults({
            "DSTORE_TEST_1": 1,
            "DSTORE_TEST_2": 2,
            "DSTORE_TEST_3": 3,
            "DSTORE_TEST_4": 4,
            "SOMETHING_ELSE": False
        })

        opts = self.store.get_configs()

