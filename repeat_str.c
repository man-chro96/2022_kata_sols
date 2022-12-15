#include <string.h>
#include <stdio.h>
#include <stdlib.h>

char *repeat_str(size_t count, const char *src) {
    char *result;
    size_t str_len = strlen(src);
    size_t i;
    result = malloc(sizeof(char) * (str_len*count) + 1);
  strcpy(result,src);
  for (i=1;i<count;i++)
    strcat(result,src);
  return result;
  }