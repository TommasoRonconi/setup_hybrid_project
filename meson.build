#######################################################################
# Global project info

project( 'custpy',
         'cpp',
         default_options : [ 'cpp_std=c++14',
                             'buildtype=debugoptimized',
                             'warning_level=0',
                             # 'prefix=' + meson.source_root(), # + '/install',
                             'libdir=lib',
                             # 'libdir=' + meson.source_root() #'libdir=lib'
         ],
         version : '0.0.0',
         license : 'GNU GPLv3' )

root = meson.source_root()

pymod = import( 'python' )
py = pymod.find_installation()
message( ' '.join( [ 'Installing python sector in', py.get_install_dir() ] ) )

cxx = meson.get_compiler( 'cpp' )
cxx_args = [ '-fopenmp' ] # '-Wall', '-Wextra', 
# foreach cxx_arg : cxx_args
# if cxx.has_argument( cxx_arg ) 
# add_global_arguments( cxx_arg,
#                       language : 'cpp' )
# endif
# endforeach
if get_option( 'full-build' )
libdir = '/'.join( [ get_option( 'prefix' ), get_option( 'libdir' ) ] )
else
libdir = '/'.join( [ py.get_install_dir(), 'custpy', 'internal' ] )
endif

#######################################################################
# External dependencies

# OMP
# omp_dep = dependency( 'openmp',
#                       required : true )

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
