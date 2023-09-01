int min(int* array, int arrayLength)
{
  int i;
  int mini=array[0];
  for (i=0;i<arrayLength;i++){
       if (array[i]<mini)
           mini=array[i];
    }
  return mini;
}

int max(int* array, int arrayLength)
{
  int i;
  int maxi=array[0];
    for (i=0;i<arrayLength;i++){
       if (array[i]>maxi) maxi=array[i];
      }
             
  return maxi;
}