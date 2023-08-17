#include <string.h>
#include <ctype.h>
void count_char_types (const char *string, unsigned *counts)
{
   int j;
   for(j=0;j<4;j++){
     *(counts+j)=0;
   }
  size_t s=strlen(string),i;
  for (i=0;i<s;i++){
    if(isupper(string[i])){ (*(counts))++; continue;}
    if (islower(string[i])) {(*(counts+1))++; continue;}
    if (isdigit(string[i])) {(*(counts+2))++; continue;}
    (*(counts+3))++;
  }
  
}