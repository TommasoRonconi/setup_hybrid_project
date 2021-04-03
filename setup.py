import setuptools
import os
import sys
import subprocess
import pathlib

from setuptools import setup as orig_setup
from setuptools import setup, find_packages, Extension
import distutils.command.build as orig_build
from setuptools.command.egg_info import egg_info as orig_egg_info
# from setuptools.command.egg_info import manifest_maker as orig_mm
# from setuptools.command.egg_info import FileList as orig_FileList
# from setuptools.command.build_ext import build_ext as build_ext_orig
import setuptools.command.install as orig_install
#from distutils.command.build import build as build_orig

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
    list_files = []
    pass

class build ( orig_build.build ) :

    def run ( self ) :

        # print( self.distribution. )
        cwd = pathlib.Path().absolute()
        print( '\n-----------------------------> TOMI CWD: ' + str( cwd ) + '\n' )
        print( subprocess.run( [ 'ls', str( cwd ) ], capture_output=True ).stdout.decode() )

        build_temp = pathlib.Path( self.build_temp )
        build_temp.mkdir( parents = True, exist_ok = True )
        # meson_args = [  '-Dprefix=' + os.sep.join( [ str(cwd), 'install' ] ) ]
        meson_args = [ '-Dprefix=' + sys.prefix ]

        os.chdir( str( build_temp ) )
        self.spawn( [ 'meson', str( cwd ) ] + meson_args )
        self.spawn( [ 'meson', 'install' ] )
        list_cmd = subprocess.run( [ 'meson', 'introspect', '--installed'  ], capture_output = True )
        Files.list_files = list( eval( list_cmd.stdout.decode().replace( '\n', '' ) ).values() )
        # print( '\n-----------------------------> TOMI PRINTS the files:' )
        # for f in Files.list_files :
        #     print( f )
        # print( '\n' )
        # with open( os.sep.join( [ str( cwd ), 'MANIFEST.in' ] ), 'a' ) as manifest:
        #     for f in Files.list_files :
        #         manifest.write( 'include ' + f + '\n')
        # print( subprocess.run( [ 'ls', str( cwd ) ], capture_output=True ).stdout.decode() )
        # print( 'tomi prints the files:\n', Files.list_files )
        os.chdir( str( cwd ) )

class install ( orig_install.install ) :

    def run ( self ) :
        print(  '\n-----------------------------> TOMI SAYS dir:\n ', dir( self ), '\n' )
        print(  '\n-----------------------------> TOMI SAYS prefix:\n ', self.prefix, '\n' )
        print(  '\n-----------------------------> TOMI SAYS help:\n ', help( self.copy_file ), '\n' )
        
        super().run()
        for f in Files.list_files :
            self.copy_file( f, f )
        # print(  '\n-----------------------------> TOMI SAYS install_base: ', self.install_base, '\n' )
        # print(  '\n-----------------------------> TOMI SAYS install_pure: ', self.install_purelib, '\n' )
        # print(  '\n-----------------------------> TOMI SAYS install_plat: ', self.install_platlib, '\n' )
        # print(  '\n-----------------------------> TOMI SAYS root: ', self.root, '\n' )

class egg_info ( orig_egg_info ) :
    
    def run (self) :
        # print( '\n-----------------------------> TOMI SAYS RUN!!\n' )
        super().run()
        # print( '\n-----------------------------> TOMI SAYS DONE!!\n' )

    def find_sources (self) :
        # print( '\n-----------------------------> Searching sources:\n' ) 
        super().find_sources()
        # print( '\n----------------------------->\n' )
        # subprocess.run( [ 'echo', '\n'.join( Files.list_files ) ], capture_output=True ).stdout
        # subprocess.run( [ 'cat', self.filelist.files[2] ], capture_output=True ).stdout
        # print( '\n-----------------------------> TOMI appends his files!!\n' )
        #self.filelist.extend( Files.list_files )
        # print( "\n-----------------------------> TOMI's egg contains:\n",
        #        '\n'.join( self.filelist.files ),
        #        "\nAll-files:\n",
        #        self.filelist.allfiles, "\n" )

# class manifest_maker ( orig_mm ) :

#     def run ( self ) :
#         self.filelist = orig_FileList()
#         if not os.path.exists(self.manifest):
#             self.write_manifest()  # it must exist so it'll get in the list
#         self.add_defaults()
#         if os.path.exists(self.template):
#             self.read_template()

#         # this is what I added:
#         self.filelist.append( Files.list_files )
#         print( 'tomi says HI!!!!1!' )
        
#         self.prune_file_list()
#         self.filelist.sort()
#         self.filelist.remove_duplicates()
#         self.write_manifest()

dist = setup( name='custpy',
              version='0.0.0',
              author='tomi',
              description='An example of hybrid C++/C/Python library installed with Meson BS',
              # packages=setuptools.find_packages( "python_sector" ),
              # package_dir={"":"."},
              data_files=[ ( sys.prefix, [ os.path.relpath( f, sys.prefix ) for f in Files.list_files ] ) ],
              include_package_data=True,
              # package_data={ '.' : Files.list_files },
              cmdclass = { 'install' : install, 'build' : build, 'egg_info' : egg_info }, #, 'manifest_maker' : manifest_maker
              # cmdclass = { 'install' : install },
              # cmdclass = dict( build_ext = build_ext ),
)

#print( dist.Location )
# sbp = subprocess.run( [ 'cat', ] )
import site
print( 'tomi has finished his job in ', site.getsitepackages() )
# for f in Files.list_files :
#     print( f )
