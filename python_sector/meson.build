#######################################################################
# Python wrapping

conf_data = configuration_data()
if get_option( 'full-build' )
conf_data.set( 'CUSTOM_PACK_WRAP', custom_pack_c_path )
wrapdir = '/'.join( [ py.get_install_dir(), 'custpy', 'internal' ] )
else
conf_data.set( 'CUSTOM_PACK_WRAP', './' + custom_pack_c_lib_name )
wrapdir = libdir
endif

configure_file( output : 'cwrap.py',
                input : 'cwrap.py.in',
                configuration : conf_data,
                install : true,
                install_dir : wrapdir )

py.install_sources( [ 'custpy/__init__.py',
                      'custpy/cust.py' ],
                    subdir : 'custpy' )

py.install_sources( [ 'custpy/internal/__init__.py' ],
                    subdir : 'custpy/internal' )

#######################################################################
