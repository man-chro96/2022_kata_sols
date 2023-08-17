#include <string.h>
#include <ctype.h>
#include <stdlib.h>
unsigned sum_string_integers (const char *string)
{
 int i;
 unsigned pow=1,sum=0;
 int s=strlen(string);
 for(i=s;i>-1;i--){
   if(isdigit(string[i])){
     sum+=pow*(string[i]-'0');
      pow*=10;
   }
   else pow=1;
     
 }
  return sum;
}