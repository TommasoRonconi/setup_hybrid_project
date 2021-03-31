#######################################################################
# Python wrapping

# pymod = import( 'python' )
# py = pymod.find_installation()
# message( py.get_install_dir() )

conf_data = configuration_data()
# conf_data.set( 'CUSTOM_PACK_WRAP', custom_pack_c_path )
conf_data.set( 'CUSTOM_PACK_WRAP', custom_pack_c_lib_name )

configure_file( output : 'cwrap.py',
                input : 'cwrap.py.in',
                configuration : conf_data,
                install : true,
                install_dir : get_option( 'libdir' ) )
                # install_dir : py.get_install_dir() + 'custpy/internal/' )

# py.install_sources( [ 'custpy/__init__.py',
#                       'custpy/cust.py' ],
#                     subdir : 'custpy' )

# py.install_sources( [ 'custpy/internal/__init__.py' ],
#                     subdir : 'custpy/internal' )

#######################################################################
