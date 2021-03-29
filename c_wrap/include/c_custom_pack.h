#ifndef __C_CUSTOM_PACK_H__
#define __C_CUSTOM_PACK_H__

#include <stddef.h>

#ifdef __cplusplus
extern "C" {
#endif

  void c_func1 ( const float a1, const float a2 );
  double c_func2 ( const double a1 );
  
#ifdef __cplusplus
} // endextern "C"
#endif
  
#endif //__C_CUSTOM_PACK_H__
