#######################################################################
# Defining local variables

root_cpp = root + '/cpp_sector'

#######################################################################
# Internal includes

inc_dir = 'include'

inc_custom_pack = include_directories( inc_dir )

#######################################################################
# CUSTOM_PACK Lib

if get_option( 'full-build' )
custom_pack_lib = library( 'custom_pack',
                           [ 'src/custom_pack.cpp' ], 
       	 	           include_directories : [ inc_custom_pack ],
		           dependencies : [],
                           install : true,
                           install_dir : libdir )
lib_headers += [ root_cpp + '/' + inc_dir + '/custom_pack.h' ]
else
custom_pack_lib = static_library( 'custom_pack',
                                  [ 'src/custom_pack.cpp' ],
       	 	                  include_directories : [ inc_custom_pack ],
		                  dependencies : [],
                                  install : true,
                                  install_dir : libdir )
endif

custom_pack_dep = declare_dependency( link_with : custom_pack_lib,
                                      include_directories : inc_custom_pack )

#######################################################################
