#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool alphanumeric(const char* strin) {
    size_t l=strlen(strin);
    bool flag=false;
    for(size_t i=0;i<l;i++){
      flag=true;
      if (!(isalpha(strin[i]) || isdigit(strin[i]))) return false;
    }
    return flag;

}