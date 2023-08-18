#include <stdbool.h>
#include <string.h>
#include <ctype.h>

bool alphanumeric(const char* string) {
    size_t l = strlen(string);
    bool flag = false;
    for(size_t i = 0; i < l; i++){
      flag = true;
      if (!(isalpha(string[i]) || isdigit(string[i]))) return false;
    }
    return flag;
}