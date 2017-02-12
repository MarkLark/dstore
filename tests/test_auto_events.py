from dstore import Model, var, mod
from dstore.Model import ModelEvents
from nose.tools import ok_
from . import BaseTest


class TestModel( Model ):
    _namespace = "test.model"
    _vars = [
        var.RowID,
        var.String( "tag", 10, mods = [ mod.NotNull(), mod.Unique() ]),
        var.String( "name", 32, mods = [ mod.NotNull() ]),
        var.Text( "description", default = "" ),
    ]

    @staticmethod
    def before_add(event, model, instance ): pass

    @staticmethod
    def after_add( event, model, instance ): pass

    @staticmethod
    def before_delete( event, model, instance ): pass

    @staticmethod
    def after_delete( event, model, instance ): pass

    @staticmethod
    def before_update( event, model, instance ): pass

    @staticmethod
    def after_update( event, model, instance ): pass

    @staticmethod
    def before_validate( event, model, instance ): pass

    @staticmethod
    def after_validate( event, model, instance ): pass

    @staticmethod
    def before_all( event, model ): pass

    @staticmethod
    def after_all( event, model, instances ): pass

    @staticmethod
    def before_get( event, model, row_id ): pass

    @staticmethod
    def after_get( event, model, instance ): pass

    @staticmethod
    def before_empty( event, model ): pass

    @staticmethod
    def after_empty( event, model ): pass

    @staticmethod
    def before_create( event, model ): pass

    @staticmethod
    def after_create( event, model ): pass

    @staticmethod
    def before_destroy( event, model ): pass

    @staticmethod
    def after_destroy( event, model ): pass

    @staticmethod
    def before_filter( event, model, params ): pass

    @staticmethod
    def after_filter( event, model, instances, params ): pass


class AutoEvent( BaseTest ):
    models = [ TestModel ]

    def test( self ):
        for name in ModelEvents._events:
            event = TestModel.events.get(name)
            func  = getattr(TestModel, name)
            ok_( func in event.listeners, "AutoEvent for TestModel.%s was not registered to listen" % name)
