#!/usr/bin/python
import pyman
from os import getcwd, path


class VM( pyman.Page ):
    def __init__( self, pkg ):
        super( VM, self ).__init__( "VM" )
        self.host = None
        self.pkg  = pkg
        self.dir = path.split( getcwd() )[1]

    def choices( self ):
        if not self.actions:
            try:
                self.host = raw_input( "Host [user@]ip: " )
            except NameError:
                self.host = input( "Host [user@]ip: " )
            self.init_actions()

        return super( VM, self ).choices()

    def init_actions( self ):
        self.add([
            pyman.Actions.Cmd( "Push Code",        "rsync -aP --delete . %s:~/%s" % ( self.host, self.dir ) ),
            pyman.Actions.Cmd( "Pull Code",        "rsync -aP %s:~/%s/ ." % ( self.host, self.dir ) ),
            pyman.Actions.Cmd( "Test",             'ssh -t %s "cd ~/%s; time nosetests -v --cover-branches --with-coverage --cover-erase --cover-package=%s --cover-html"' % ( self.host, self.dir, self.pkg ) ),
            pyman.Actions.Cmd( "Test With Stdout", 'ssh -t %s "cd ~/%s; time nosetests -vs --cover-branches --with-coverage --cover-erase --cover-package=%s --cover-html"' % ( self.host, self.dir, self.pkg) ),
            pyman.Actions.Cmd( "Pull Coverage",    "rsync -aP %s:~/%s/cover/ cover/ &> /dev/null; google-chrome cover/index.html" % ( self.host, self.dir ) ),
            pyman.Actions.Cmd( "Open Coverage",    "google-chrome cover/index.html" ),
            pyman.Actions.Cmd( "PyTerm",           'ssh -t %s "cd ~/%s; python"' % ( self.host, self.dir ) ),
            pyman.Actions.Cmd( "Install Package",  'ssh -t %s "cd ~/%s; sudo python setup.py develop"' % ( self.host, self.dir ) ),
            pyman.Actions.Back()
        ])

menu = pyman.Main( "DStore - Manager", [
    VM( "dstore" ),
    pyman.Doc(),
    pyman.PyPi(),
    pyman.NoseTest(),
    pyman.Git(),
    pyman.Actions.Exit()
])
menu.cli()
