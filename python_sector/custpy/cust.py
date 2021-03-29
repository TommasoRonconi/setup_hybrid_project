from .internal.cwrap import *

def pyfunc1 ( a1, a2 ) :
    lib_cust.c_func1( c_float( a1 ), c_float( a2 ) )
    return;

def pyfunc2 ( a1 ) :
    return float( lib_cust.c_func2( c_double( a1 ) ) )
