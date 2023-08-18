#include <string>

std::string pofi(unsigned n)
{
      if ((n - 3) % 4 == 0)
            return "-i";
      if ((n - 2) % 4 == 0)
            return "-1";
      if ((n - 1) % 4 == 0)
            return "i";
      return "1";
}