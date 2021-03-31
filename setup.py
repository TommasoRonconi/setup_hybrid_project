import setuptools
import os
import re
import sys
import subprocess
import pathlib

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig

# class MesonExtension ( Extension ) :
#     def __init__ ( self, name, sourcedir = '' ) :
#         Extension.__init__( self, name, sources = [] )
#         if hasattr( sourcedir, "__len__" ) :
#             self.sourcedir = [ os.path.abspath( sd ) for sd in sourcedir ]
#         else :
#             self.sourcedir = os.path.abspath( sourcedir )

class MesonExtension ( Extension ) :
    def __init__ ( self, name ) :
        super().__init__( name, sources = [] )
        # Extension.__init__( self, name, sources = [] )
        # self.sourcedir = os.path.abspath( sourcedir )

class build_ext( build_ext_orig ) :

    def run ( self ) :
        for ext in self.extensions :
            self.build_meson( ext )
        # super().run()

    def build_meson ( self, ext ) :

        cwd = pathlib.Path().absolute()

        build_temp = pathlib.Path( self.build_temp )
        build_temp.mkdir( parents = True, exist_ok = True )
        extdir = pathlib.Path( self.get_ext_fullpath( ext.name ) )
        extdir.mkdir( parents = True, exist_ok = True )
        meson_args = [ '-Dprefix=' + str( extdir.parent.absolute() ),
                       '-Dlibdir=./internal']

        os.chdir( str( build_temp ) )
        self.spawn( [ 'meson', str( cwd ) ] + meson_args )
        self.spawn( [ 'meson', 'install' ] )
        # if not self.dry_run :
        #    self.spawn
        os.chdir( str( cwd ) )
        
# class mesonbuild_ext ( build_ext ) :
#     def run ( self ) :
#         # for ext in self.extensions :
#         #     self.build_extension( ext )
#         print( 'tomi calling super(...).run()' )
#         super( mesonbuild_ext, self ).run()

#     def build_extension( self, ext ) :
#         print( 'tomi says hi!' )
        
#         subprocess.check_call( [ 'meson',
#                                  'builddir', ] )
#         subprocess.call( [ 'meson', 'install', '-C', 'builddir' ])
#         print( 'tomi calling super(...).build_extension()' )
#         #super( mesonbuild_ext, self ).build_extension( ext )
#         # setuptools.command.build_ext
#         # '='.join( [ '-Dprefix', os.path.dirname(os.path.abspath('.')) ] )
        
# class MesonBuild ( build_ext ) :
#     def run ( self ) :
#         # try :
#         #     out = subprocess.run( [ 'meson', '--version' ], capture_output = True )
#         # except OSError :
#         #     raise RuntimeError(
#         #         "The Meson build system must be installed to build the following extensions: " +
#         #         ", ".join( e.name for e in self.extensions ) )
#         # meson_version = str( out.stdout.decode() ).replace( '\n', '' )
#         # if meson_version > '0.56.2' :
#         #     raise RuntimeError( "Meson <= 0.56.2 is required." )

#         for ext in self.extensions :
#             self.build_extensions( ext )

#         return;

#     def build_extensions ( self, ext ) :

#         print( 'tomi says: ', os.path.dirname( os.path.abspath(__file__) ) )
        
#         # print( 'tomi says: ', os.path.abspath( os.path.dirname(
#         #     self.get_ext_fullpath( ext.name ) ) ) )
#         # extdir = os.path.abspath( os.path.dirname( self.get_ext_fullpath( ext.name ) ) )

#         # env = os.environ.copy()

#         # print( 'tomi says: ', self.build_temp )
#         # print( 'tomi says: ', os.path.dirname(os.path.abspath(__file__)) )
#         # if not os.path.exists( self.build_temp ) :
#         #     os.makedirs( self.build_temp )

#         print( 'tomi lists: ' )
#         subprocess.call( [ 'ls', os.path.dirname(os.path.abspath(__file__)) ] )
        
#         subprocess.check_call( [ 'meson', 'builddir', '='.join( ['-Dprefix', os.path.dirname(os.path.abspath(__file__)) + '/python_sector/custpy/internal/core' ] ) ] )
#         subprocess.call( [ 'meson', 'install', '-C', 'builddir' ] )

# cwd = os.path.dirname(os.path.abspath(__file__))

# setup( name='custpy',
#        version='0.0.0',
#        author='tomi',
#        description='An example of hybrid C++/C/Python library installed with Meson BS',
#        packages=setuptools.find_packages( "python_sector" ),
#        package_dir={"":"python_sector"},
#        package_data={'custpy' : [
#            #'internal/cwrap.py',
#            'internal/core/lib/*.so',
#            'internal/core/include/*.h',
#        ]
#        },
#        ext_modules=[MesonExtension('custpy.internal')],
#        cmdclass=dict(build_ext=MesonBuild)
# )

###########################################################################################
cwd = os.path.dirname(os.path.abspath(__file__))

include_custom_pack = [ cwd + '/cpp_sector/include' ]
module_custom_pack = Extension( 'custpy.internal.libcustom_pack',
                                language="c++14",
                                sources=["cpp_sector/src/custom_pack.cpp"],
                                libraries=[],
                                extra_compile_args=['-std=c++14', '-Wall', '-Wextra'],
                                include_dirs=include_custom_pack )

include_c_custom_pack = include_custom_pack + [ cwd + '/c_wrap/include' ]
module_c_custom_pack = Extension( 'custpy.internal.libc_custom_pack',
                                  language="c++14",
                                  sources=["c_wrap/src/c_custom_pack.cpp"],
                                  libraries=[],
                                  extra_compile_args=['-std=c++14', '-Wall', '-Wextra'],
                                  include_dirs=include_c_custom_pack )
###########################################################################################

# module_meson_custom_pack = MesonExtension( 'custpy/internal', runtime_library_dirs=[] )

setup( name='custpy',
       version='0.0.0',
       author='tomi',
       description='An example of hybrid C++/C/Python library installed with Meson BS',
       #py_modules=[ 'custpy' ],
       packages=setuptools.find_packages( "python_sector" ),
       package_dir={"":"python_sector"},
       package_data={'custpy' : [
           'custpy/internal/cwrap.py',
           'custpy/internal/*.so',
       ]
       },
       include_package_data=True,
       # ext_modules=[MesonExtension('custpy.internal')],
       #cmdclass = dict( build_ext = build_ext ),
       ext_modules = [
           # module_meson_custom_pack,
           module_custom_pack,
           module_c_custom_pack,
       ],
       #ext_package='',
)
