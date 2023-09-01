#include <math.h>

unsigned long long square_digits(unsigned n) {
  unsigned long long squaredig = 0;
   unsigned long long power = 1;
while (n>0) {
    unsigned digit = n % 10;
    unsigned square = pow(digit,2);
    squaredig += square * power;
    if (square < 10)  power =power* 10;
    else  power=power* 100;
    n =n / 10;
  }
  return squaredig;
}