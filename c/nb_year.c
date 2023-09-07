#include <math.h>
int nbYear(int p0, double percent, int aug, int p) {
    int i = 0;
    double sum = p0;
    while(sum < p) {
      sum=sum*(1+(percent/100))+aug;
      sum=floor(sum);
      i += 1;
    }
  return i;
}