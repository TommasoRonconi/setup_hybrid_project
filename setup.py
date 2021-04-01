import setuptools
import os
import re
import sys
import subprocess
import pathlib

from setuptools import setup, find_packages, Extension
from setuptools.command.build_ext import build_ext as build_ext_orig
from setuptools.command.install import install as install_orig
from distutils.command.build import build as build_orig

# Method obtained modifying this:
# https://stackoverflow.com/questions/42585210/extending-setuptools-extension-to-use-cmake-in-setup-py/48015772

# class install ( install_orig ) :

#     def run ( self ) :

#         cwd = pathlib.Path().absolute()

#         build_temp = pathlib.Path( self.build_temp )
#         build_temp.mkdir( parents = True, exist_ok = True )
#         extdir = pathlib.Path( self.get_ext_fullpath( ext.name ) )
#         extdir.mkdir( parents = True, exist_ok = True )
#         meson_args = [ '-Dprefix=' + sys.prefix ]

#         os.chdir( str( build_temp ) )
#         self.spawn( [ 'meson', str( cwd ) ] + meson_args )
#         self.spawn( [ 'meson', 'install' ] )
#         os.chdir( str( cwd ) )
#         super().run()

class build ( build_orig ) :

    def run ( self ) :

        cwd = pathlib.Path().absolute()

        build_temp = pathlib.Path( self.build_temp )
        build_temp.mkdir( parents = True, exist_ok = True )
        # extdir = pathlib.Path( self.get_ext_fullpath( ext.name ) )
        # extdir.mkdir( parents = True, exist_ok = True )
        meson_args = [ '-Dprefix=' + sys.prefix ]

        os.chdir( str( build_temp ) )
        self.spawn( [ 'meson', str( cwd ) ] + meson_args )
        self.spawn( [ 'meson', 'install' ] )
        os.chdir( str( cwd ) )
   
# class MesonExtension ( Extension ) :
#     def __init__ ( self, name ) :
#         super().__init__( name, sources = [] )

# class build_ext( build_ext_orig ) :

#     def run ( self ) :
#         for ext in self.extensions :
#             self.build_meson( ext )

#     def build_meson ( self, ext ) :

#         cwd = pathlib.Path().absolute()

#         build_temp = pathlib.Path( self.build_temp )
#         build_temp.mkdir( parents = True, exist_ok = True )
#         extdir = pathlib.Path( self.get_ext_fullpath( ext.name ) )
#         extdir.mkdir( parents = True, exist_ok = True )
#         meson_args = [ '-Dprefix=' + str( extdir.parent.absolute() ),
#                        '-Dlibdir=./internal',
#                        '-Dfull-build=false' ]

#         os.chdir( str( build_temp ) )
#         self.spawn( [ 'meson', str( cwd ) ] + meson_args )
#         self.spawn( [ 'meson', 'install' ] )
#         os.chdir( str( cwd ) )

# module_meson_custom_pack = MesonExtension( 'custpy/internal' )

setup( name='custpy',
       version='0.0.0',
       author='tomi',
       description='An example of hybrid C++/C/Python library installed with Meson BS',
       # packages=setuptools.find_packages( "python_sector" ),
       package_dir={"":"."},
       # package_data={'custpy' : [
       #     'custpy/internal/cwrap.py',
       #     'custpy/internal/*.so',
       # ]
       # },
       # include_package_data=True,
       cmdclass = { 'build' : build },
       # cmdclass = { 'install' : install },
       # cmdclass = dict( build_ext = build_ext ),
       # ext_modules = [
       #     module_meson_custom_pack,
       # ],
)
