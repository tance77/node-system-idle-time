const system = require("./addon");

setInterval(function () {
  //Returns time in milliseconds
  console.log(system.getIdleTime());
}, 1000);
