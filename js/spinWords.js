function ReverseString(str) {
   return str.split('').reverse().join('');
}

function spinWords(string){
 string = string.split(" ");
 for(let i = 0 ; i < string.length; i++){
   if(string[i].length >= 5){
     string[i] = ReverseString(string[i]);
   }
 }
 return string.join(" ");
}