function testIt(arr) {
   let max = Math.max(...arr);
   let min = Math.min(...arr);
   let newarr = arr.filter(elem => elem !== max && elem !== min)
   if (newarr.length === 0 ){
     return 0;
   }
   return Math.round(100 * newarr.reduce((acc, cv) => acc+cv, 0)/ newarr.length) / 100;
 }