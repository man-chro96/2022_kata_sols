int multiples3_5(int n) {
		int sum=0,i;
    if (n<=0){
      return 0;
    }
    for(i=n-1;i>0;i--){
      if ((i%3==0 || i%5==0)){
        sum+=i;
      }
    }
    return sum;
}