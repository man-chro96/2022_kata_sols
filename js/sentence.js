//https://www.codewars.com/kata/5b047875de4c7f9af800011b/train/javascript

export default function sentence(List) {
  
   const objectList = {};
  
   List.forEach((x) => {
      const key = Object.keys(x)[0];
      const value = x[key];
      objectList[key] = value;
   })
  
   return List.map(x => Object.keys(x)[0]).sort((a,b) => a - b).map(x => objectList[x]).join(' ');
}