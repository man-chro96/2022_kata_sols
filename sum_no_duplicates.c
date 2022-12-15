#include <stddef.h>
#include <stdbool.h>

int sum_no_duplicates(size_t length, const int array[length]) {
        
  int sum=0;
  bool flag;
  
  for(size_t i = 0; i < length; i++){
    flag=false;
    for(size_t j=0; j < length; j++){
      if (j != i ) {
        if (array[i]==array[j]) flag=true;
          }
    }
    if(flag==false) sum+=array[i];
  }
  return sum;
}