import setuptools
import os
import sys
import subprocess
import pathlib

from setuptools import setup as orig_setup
from setuptools import setup, find_packages, Extension
import distutils.command.build as orig_build
from setuptools.command.egg_info import egg_info as orig_egg_info
import setuptools.command.install as orig_install

# Method obtained modifying this:
# https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py/48015772
# and this
# https://stackoverflow.com/questions/46333210/how-to-include-script-built-libraries-with-package-installation

def setup(**attrs) :
    from distutils.core import Distribution
    klass = attrs.get('distclass')
    if klass :
        print( type( klass ) )
    else :
        print( type( Distribution ) )

    return orig_setup(**attrs)

class Files () :
    """ This is just for defining a class-attribute (~static)
    Not knowing who is calling and passing what to who, in this
    way I know any modification to the list_files attribute will be visible
    to the whole 'runtime'
    """
    list_files = []
    pass

class build ( orig_build.build ) :
    """ This overriding here actually works, problem is the 
    generated files.
    (the build is not aware of the python nor of the compiled c++/c sectors)
    I'll end up with a lot of files installed but no tracking on them
    for uninstalling. To make the matters worse, when the build is
    complete pip removes the build directory, so we are completely 
    left with no way of tracking back what happened.
    """

    def run ( self ) :

        cwd = pathlib.Path().absolute()
        print( subprocess.run( [ 'ls', str( cwd ) ], capture_output=True ).stdout.decode() )

        build_temp = pathlib.Path( self.build_temp )
        build_temp.mkdir( parents = True, exist_ok = True )
        meson_args = [ '-Dprefix=' + sys.prefix ]

        os.chdir( str( build_temp ) )
        # this builds the meson configuration
        self.spawn( [ 'meson', str( cwd ) ] + meson_args )
        # this installs in the system prefix
        self.spawn( [ 'meson', 'install' ] )
        # I introspect the meson build to obtain a list of insalled files (with the correct absolute paths)
        list_cmd = subprocess.run( [ 'meson', 'introspect', '--installed'  ], capture_output = True )
        # the list is in binary strings and contains a newline character at the end so it requires some manipulation
        Files.list_files = list( eval( list_cmd.stdout.decode().replace( '\n', '' ) ).values() )
        os.chdir( str( cwd ) )

class install ( orig_install.install ) :
    """ This override here is completely superflous
    """

    def run ( self ) :
        super().run()
        # I thought that maybe by making the installer
        # copy the files into themselves I could convince
        # it about their existence. It did not work.
        for f in Files.list_files :
            self.copy_file( f, f )

class egg_info ( orig_egg_info ) :
    """ This override here is completely superflous
    """
    
    def run (self) :
        super().run()

    def find_sources (self) :
        super().find_sources()

dist = setup( name='custpy',
              version='0.0.0',
              author='tomi',
              description='An example of hybrid C++/C/Python library installed with Meson BS',
              data_files=[ ( sys.prefix, [ os.path.relpath( f, sys.prefix ) for f in Files.list_files ] ) ],
              include_package_data=True,
              cmdclass = { 'install' : install, 'build' : build, 'egg_info' : egg_info }, 
)
