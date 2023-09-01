int numdig(int n){
  int count=0;
   do {
    n /= 10;
    ++count;
  } while (n != 0);
    return count;
}

int digital_root(int n) {
  int numsum=0;
  int i;
  if(numdig(n)==1) return n;
  int x=n;
  for (i=0;i<numdig(n);i++){
    numsum+=x % 10;
    x=x/10;
    }
  return digital_root(numsum);
  }
  
    