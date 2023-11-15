export default function stringSplit(str) {
   return str == "" ? [] : (str.length % 2 == 0 ? str : str + "_").match(/.{2}/g);
}