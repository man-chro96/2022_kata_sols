function trim(str, size) {
   if(size >= str.length) return str;
   if(size <= 3) return str.slice(0,size) + "..."
   return str.slice(0, size-3) + "..."
 }