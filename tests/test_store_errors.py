from nose.tools import raises
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
    @raises( MNR )
    def test_all( self ):
        self.store.all( TestModel )

    @raises( MNR )
    def test_add( self ):
        self.store.add( TestModel( test = 123 ) )

    @raises( MNR )
    def test_delete( self ):
        self.store.delete( TestModel( id = 1 ) )

    @raises(MNR)
    def test_update( self ):
        self.store.update( TestModel( id = 0, test = 456 ) )

    @raises(MNR)
    def test_get( self ):
        self.store.get( TestModel, 0 )

    @raises(MNR)
    def test_empty( self ):
        self.store.empty( TestModel )

    @raises(MNR)
    def test_create( self ):
        self.store.create( TestModel )

    @raises(MNR)
    def test_destroy( self ):
        self.store.destroy( TestModel )

    @raises(MNR)
    def test_filter( self ):
        self.store.filter( TestModel, test = 456 )


class InstanceNotFound( BaseTest ):
    @raises( INF )
    def test_get( self ):
        Car.get( 0 )

    @raises(INF)
    def test_filter( self ):
        Car.filter( manufacturer = "Something", make = "New" )


class IncompatibleSource( BaseTest ):
    @raises( IS )
    def test_models( self ):
        Car().set( TestModel() )

    @raises(IS)
    def test_list( self ):
        Car().set( [ 1, 2, 3 ] )

    def test_already_assigned( self ):
        car = Car( manufacturer = "Holden", make = "Rodeo", year = 2002 )
        car.set( { "make": "Commodore" } )


class ModelNotFound( BaseTest ):
    @raises( MNF )
    def test_get_model( self ):
        self.store.get_model("cars.something")


class VariableNotFound( BaseTest ):
    @raises( VNF )
    def test_get_var( self ):
        Car.get_var( "many" )

    @raises( VNF )
    def test_get_var_type( self ):
        Car.get_var( "manufacturer", "Number" )
