#######################################################################
# Defining local variables

root_cpp = root + '/cpp_sector'

#######################################################################
# Internal includes

inc_dir = 'include'

inc_custom_pack = include_directories( inc_dir )

#######################################################################
# SFH Lib

custom_pack_lib = library( 'custom_pack',
                           [ 'src/custom_pack.cpp' ],
       	 	           include_directories : [ inc_custom_pack ],
		           dependencies : [],
                           install : true,
                           install_dir : libdir )

custom_pack_dep = declare_dependency( link_with : custom_pack_lib,
                                      include_directories : inc_custom_pack )

if get_option( 'full-build' )
lib_headers += [ root_cpp + '/' + inc_dir + '/custom_pack.h' ]

#######################################################################
# Further installation commands

install_headers( lib_headers )
endif

#######################################################################
