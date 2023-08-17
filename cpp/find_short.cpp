#include <string>
#include <cctype>
int find_short(std::string str)
{
  int glob=0;
  for (char y:str){
    if(isspace(y)) break;
    glob++;
    
  }
  int count=glob;
  for (char c : str)
  {
    if(isspace(c))
       { 
          if(count<=glob) glob=count;
          count=0;
      }
                   
    else count++;
    
  }
  if (count<glob) glob=count;
  return glob;
}