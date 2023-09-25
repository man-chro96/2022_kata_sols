function findOdd(array) {
   const memo = {};
   for (let i of array) {
     if (typeof memo[String(i)] === 'undefined') {
       memo[String(i)] = 0;
     }
     memo[String(i)]++;
   }
   for (const value of Object.values(memo)) {
     if (value % 2 !== 0) {
       return Number(Object.keys(memo)[Object.values(memo).indexOf(value)])
     }
   }
 }