#include <c_custom_pack.h>
#include <custom_pack.h>
#include <iostream>

extern "C" {

  void c_func1 ( const float a1, const float a2 ) {

    std::cout << "ehi from C\n";
    cust::func1( a1, a2 );
    return;

  }

  double c_func2 ( const double a1 ) {

    std::cout << "ehi from C\n";
    return cust::func2( a1 );

  }  

} // endextern "C"
