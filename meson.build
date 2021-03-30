#######################################################################
# Global project info

project( 'master',
         'cpp',
         default_options : [ 'cpp_std=c++14',
                             'buildtype=debugoptimized',
                             #'prefix=' + meson.source_root() + '/install',
                             'libdir=lib' ],
         version : '0.0.0',
         license : 'SISSA' )

root = meson.source_root()

cxx = meson.get_compiler( 'cpp' )

cxx_args = [ '-Wall',
             '-Wextra' ] #, '-fopenmp'

foreach cxx_arg : cxx_args
if cxx.has_argument( cxx_arg ) 
add_global_arguments( cxx_arg,
                      language : 'cpp' )
endif
endforeach

#######################################################################
# External dependencies

# OMP
# omp_dep = dependency( 'openmp',
#                       required : true )

#######################################################################
# Empty list to append headers (from both C++ and C sectors)

lib_headers = []

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
