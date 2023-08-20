function isVowel(x) { 
   return ("aeiouAEIOU".indexOf(x) != -1); 
 }
 
 function isAlpha(x){
   return /^[A-Z]$/i.test(x);
 }
 
 function consonantCount(str) {
   let sum = 0;
   for( const i of str) {
     if (isVowel(i)  || !(isAlpha(i)))  sum++;
     }
     return str.length-sum;
 }