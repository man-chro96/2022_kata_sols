const cleanText = (text) => {
   return text.replace(/[^a-zA-Z']/g, ' ');
}

const removeAllWhitespaces = (arr) => {
   let indexToRemove;

   while((indexToRemove = arr.indexOf('')) !== -1) {
      arr.splice(indexToRemove, 1)
   }

   return arr;
}

const createRecurrenceMap = (arr) => {
   const recurrenceMap = {};
   for (const el of arr) {
      if (!recurrenceMap[el]) {
         recurrenceMap[el] = 1;
      } else {
         recurrenceMap[el]++;
      }
   }

   return recurrenceMap;
}

const getTopKeys = (obj, topCount) => {
   let entries = Object.entries(obj);

   entries.sort((a,b) => b[1] - a[1]);

   let topKeys = entries.slice(0, topCount).map(entry => entry[0]);

   return topKeys;
}


function topThreeWords(text) {
    let nonLetterRegex = /^[^a-zA-Z]*$/;

   if (nonLetterRegex.test(text)) return [];
  
   let cleanedText = cleanText(text.toLowerCase());
   let arrayOfSplitWords = cleanedText.split(' ');
   let modifiedArray = removeAllWhitespaces(arrayOfSplitWords);
   let recurrenceObject = createRecurrenceMap(modifiedArray);
  
   return getTopKeys(recurrenceObject, 3);
}
