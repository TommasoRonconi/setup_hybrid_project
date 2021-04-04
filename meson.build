#######################################################################
# Global project info

project( 'custpy',
         'cpp',
         default_options : [ 'cpp_std=c++14',
                             'buildtype=debugoptimized',
                             'warning_level=0',
                             'libdir=lib',
         ],
         version : '0.0.0',
         license : 'GNU GPLv3' )

root = meson.source_root()

pymod = import( 'python' )
py = pymod.find_installation()
message( ' '.join( [ 'Installing python sector in', py.get_install_dir() ] ) )

if get_option( 'full-build' )
libdir = '/'.join( [ get_option( 'prefix' ), get_option( 'libdir' ) ] )
else
libdir = '/'.join( [ py.get_install_dir(), 'custpy', 'internal' ] )
endif

#######################################################################
# Empty list to append headers (from both C++ and C sectors)

if get_option( 'full-build' )
         lib_headers = []
endif

#######################################################################
# CPP sector

subdir( 'cpp_sector' )

#######################################################################
# C bridge

subdir( 'c_wrap' )

#######################################################################
# Python module

subdir( 'python_sector') 

#######################################################################
