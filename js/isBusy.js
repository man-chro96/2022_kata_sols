function getStatus(isBusy) {
   var msg = (isBusy ? "busy" : "available");
   return new Object(
   {
     status: msg
   })
 }