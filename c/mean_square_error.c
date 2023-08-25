#include <stddef.h>
#include <math.h>

double mean_square_error(size_t n, const int a[n], const int b[n]) {
   int i;
   double sum=0.0;
   for (i=0;i<n;i++){
     sum+=(a[i]-b[i])*(a[i]-b[i]);
   }
  return sum/n;

}