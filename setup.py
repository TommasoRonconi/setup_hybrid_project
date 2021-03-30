import setuptools
import os
import re
import sys
import subprocess

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext

# class MesonExtension ( Extension ) :
#     def __init__ ( self, name, sourcedir = '' ) :
#         Extension.__init__( self, name, sources = [] )
#         if hasattr( sourcedir, "__len__" ) :
#             self.sourcedir = [ os.path.abspath( sd ) for sd in sourcedir ]
#         else :
#             self.sourcedir = os.path.abspath( sourcedir )

# class MesonBuild ( build_ext ) :
#     def run ( self ) :
#         try :
#             out = subprocess.run( [ 'meson', '--version' ], capture_output = True )
#         except OSError :
#             raise RuntimeError(
#                 "The Meson build system must be installed to build the following extensions: " +
#                 ", ".join( e.name for e in self.extensions ) )
#         meson_version = str( out.stdout.decode() ).replace( '\n', '' )
#         # if meson_version > '0.56.2' :
#         #     raise RuntimeError( "Meson <= 0.56.2 is required." )

#         for ext in self.extensions :
#             self.build_extensions( ext )

#         return;

#     def build_extensions ( self, ext ) :

#         print( 'tomi says: ', os.path.abspath(__file__) )
        
#         print( 'tomi says: ', os.path.abspath( os.path.dirname(
#             self.get_ext_fullpath( ext.name ) ) ) )
#         extdir = os.path.abspath( os.path.dirname( self.get_ext_fullpath( ext.name ) ) )

#         env = os.environ.copy()

#         print( 'tomi says: ', self.build_temp )
#         print( 'tomi says: ', os.path.dirname(os.path.abspath(__file__)) )
#         # if not os.path.exists( self.build_temp ) :
#         #     os.makedirs( self.build_temp )

#         subprocess.check_call( [ 'meson', 'builddir' ] ) #, '='.join( '-Dprefix=', ext.sourcedir
#         subprocess.call( [ 'meson', 'install', '-C', 'builddir' ] )

cwd = os.path.dirname(os.path.abspath(__file__))

setup( name='custpy',
       version='0.0.0',
       author='tomi',
       description='An example of hybrid C++/C/Python library installed with Meson BS',
       #packages=setuptools.find_packages( "python_sector" ),
       #package_dir={"":"python_sector"},
       ext_modules=[MesonExtension('custpy.internal')],
       cmdclass=dict(build_ext=MesonBuild)
)
