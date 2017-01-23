from dstore import MemoryStore, Model, var, mod
from unittest import TestCase

__all__ = [ "BaseTest", "Car", "AllVars" ]


class Car( Model ):
    _namespace = "cars.make"
    _vars = [
        var.RowID,
        var.String( "manufacturer", 32, mods = [ mod.NotNull() ] ),
        var.String( "make", 32, mods = [ mod.NotNull() ] ),
        var.Number( "year", mods = [ mod.NotNull(), mod.Min( 1950 ), mod.Max( 2017 ) ] ),
    ]


class AllVars( Model ):
    _namespace = "all.vars"
    _vars = [
        var.RowID,
        var.Number( "number", mods = [ mod.Min( 0 ), mod.Max( 100 ) ] ),
        var.Boolean( "boolean" ),
        var.String( "string", 32, mods = [ mod.NotNull() ] ),
        var.Character( "character", 4 ),
        var.Binary( "binary", 25 ),
        var.Text( "text" ),
        var.Float( "float" ),
        var.Enum( "enum", [ "one", "two", "three" ] ),
        var.ForeignKey( "cars.make" )
    ]


class BaseTest( TestCase ):
    models      = [ Car, AllVars ]
    auto_create = True
    auto_init   = True

    def setUp( self ):
        if self.auto_init:
            self.store = MemoryStore( self.models )
            self.store.init_app()
            self.store.connect()
        if self.auto_create: self.store.create_all()

    def tearDown( self ):
        if self.auto_create: self.store.destroy_all()
        if self.auto_init:
            self.store.disconnect()
            self.store.destroy_app()
