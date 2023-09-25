export default function digitize(n) {
   return Array.from(String(n)).map(x => Number(x)).reverse();
}