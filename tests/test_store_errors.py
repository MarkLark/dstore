from nose.tools import assert_raises
from . import BaseTest, Car
from dstore import Model, var, mod
from dstore.Error import ModelNotRegistered as MNR, InstanceNotFound as INF, IncompatibleSource as IS,\
    ModelNotFound as MNF, VariableNotFound as VNF


class TestModel( Model ):
    _namespace = "test.model"
    _vars = [
        var.RowID,
        var.Number( "test", default = 0, mods = [ mod.NotNull( ) ] )
    ]


class ModelNotRegistered( BaseTest ):
    def test_all( self ):
        with assert_raises( MNR ):
            self.store.all( TestModel )

    def test_add( self ):
        with assert_raises( MNR ):
            self.store.add( TestModel( test = 123 ) )

    def test_delete( self ):
        with assert_raises( MNR ):
            self.store.delete( TestModel( id = 1 ) )

    def test_update( self ):
        with assert_raises( MNR ):
            self.store.update( TestModel( id = 0, test = 456 ) )

    def test_get( self ):
        with assert_raises( MNR ):
            self.store.get( TestModel, 0 )

    def test_empty( self ):
        with assert_raises( MNR ):
            self.store.empty( TestModel )

    def test_create( self ):
        with assert_raises( MNR ):
            self.store.create( TestModel )

    def test_destroy( self ):
        with assert_raises( MNR ):
            self.store.destroy( TestModel )

    def test_filter( self ):
        with assert_raises( MNR ):
            self.store.filter( TestModel, test = 456 )


class InstanceNotFound( BaseTest ):
    def test_get( self ):
        with assert_raises( INF ):
            Car.get( 0 )

    def test_filter( self ):
        with assert_raises( INF ):
            Car.filter( manufacturer = "Something", make = "New" )


class IncompatibleSource( BaseTest ):
    def test_models( self ):
        with assert_raises( IS ):
            Car().set( TestModel() )

    def test_list( self ):
        with assert_raises( IS ):
            Car().set( [ 1, 2, 3 ] )

    def test_already_assigned( self ):
        car = Car( manufacturer = "Holden", make = "Rodeo", year = 2002 )
        car.set( { "make": "Commodore" } )


class ModelNotFound( BaseTest ):
    def test_get_model( self ):
        with assert_raises( MNF ):
            self.store.get_model("cars.something")


class VariableNotFound( BaseTest ):
    def test_get_var( self ):
        with assert_raises( VNF ):
            Car.get_var( "many" )

        with assert_raises( VNF ):
            Car.get_var( "manufacturer", "Number" )
