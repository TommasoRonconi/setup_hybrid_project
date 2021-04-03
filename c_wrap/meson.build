#######################################################################
# Local variables

root_c = root + '/c_wrap'

#######################################################################
# Internal includes

inc_dir = 'include'

inc_c_custom_pack = include_directories( inc_dir )

#######################################################################
# Lib C interface

custom_pack_c_lib = library( 'c_custom_pack',
                             [ 'src/c_custom_pack.cpp' ],
                             include_directories : [ inc_c_custom_pack,
                                                     inc_custom_pack ],
                             dependencies : [ custom_pack_dep ],
                             install : true,
                             install_dir : libdir )

custom_pack_c_dep = declare_dependency( link_with : [ custom_pack_c_lib,
                                                      custom_pack_lib ],
                                        include_directories : [ inc_custom_pack,
                                                                inc_c_custom_pack ] )

custom_pack_c_lib_name = custom_pack_c_lib.full_path().split('/')[-1]

custom_pack_c_path = '/'.join( [ get_option( 'prefix' ),
                                 get_option( 'libdir' ),
                                 custom_pack_c_lib_name ] )

if get_option( 'full-build' )
lib_headers += [ root_c + '/' + inc_dir + '/c_custom_pack.h' ]


#######################################################################
# Further installation commands

install_headers( lib_headers )
endif

#######################################################################
