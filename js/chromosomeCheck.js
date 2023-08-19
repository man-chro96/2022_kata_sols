function chromosomeCheck(sperm) {
   gene = {
     'XY':'son',
     'XX':'daughter'
   };
   return "Congratulations! You're going to have a " + gene[sperm] + ".";
 }