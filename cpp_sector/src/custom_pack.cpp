#include <iostream>
#include <custom_pack.h>

void cust::func1 ( const float a1, const float & a2 ) {

  std::cout << "I'm func1:\t" << a1 * a2 << "\n";
  return;

}

double cust::func2 ( const double a1 ) {

  return a1 * a1 * a1;

}
