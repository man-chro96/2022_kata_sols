typedef unsigned long long ull;

ull nth_fib(int n) {
 ull a=0;
 ull b=1;
 ull x;
 int i;
 for(i=0;i<n-1;i++)
   { x=a+b;
     a=b;
     b=x;
    }
return a;
   }