#include <stdbool.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>
char *to_jaden_case (char *jaden_case, const char *string)
{
  bool flag=true;
  *jaden_case='\0';
   int temp=0;
   int ptr=0;
  while(string[temp] !='\0'){
    if (string[temp]==' ') {
      flag=true;
      jaden_case[ptr]=string[temp];
      temp++;
      ptr++;
      continue;
      }
    if (flag==true) {
      if (islower(string[temp])){
     jaden_case[ptr]=string[temp]+('A' - 'a');
        }
      else jaden_case[ptr]=string[temp];
      flag=false;
      }
    else {
      jaden_case[ptr]=string[temp];
          flag=false;
          }
    temp++;
    ptr++;
      }
  jaden_case[ptr]='\0';
  return jaden_case;  
  }