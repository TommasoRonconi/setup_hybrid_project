#######################################################################
# Python wrapping

if get_option( 'full-build' )
pymod = import( 'python' )
py = pymod.find_installation()
message( ' '.join( [ 'Installing python sector in', py.get_install_dir() ] ) )
endif

conf_data = configuration_data()
if get_option( 'full-build' )
conf_data.set( 'CUSTOM_PACK_WRAP', custom_pack_c_path )
wrapdir = py.get_install_dir() + 'custpy/internal/'
else
conf_data.set( 'CUSTOM_PACK_WRAP', custom_pack_c_lib_name )
wrapdir = get_option( 'libdir' )
endif

configure_file( output : 'cwrap.py',
                input : 'cwrap.py.in',
                configuration : conf_data,
                install : true,
                install_dir : wrapdir )

if get_option( 'full-build' )
py.install_sources( [ 'custpy/__init__.py',
                      'custpy/cust.py' ],
                    subdir : 'custpy' )

py.install_sources( [ 'custpy/internal/__init__.py' ],
                    subdir : 'custpy/internal' )
endif

#######################################################################
