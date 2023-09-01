#include <stdbool.h>
#include <stddef.h>

typedef bool (*Predicate)(int);

bool none(const int* arr, size_t size, Predicate fun)
{
    unsigned i;
    bool flag=true;
    for (i=0;i<size;i++){
      if ((*fun)(arr[i])==1) flag=false ;
      }
    return flag;
    }
   