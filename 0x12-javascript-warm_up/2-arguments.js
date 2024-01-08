// exportVar.js
module.exports = {
 printMsg: function () {
    if (process.argv.length === 2) {
      console.log('No argument');
    } else if (process.argv.length === 3) {
      console.log('Argument found');
    } else {
      console.log('Arguments found');
    }
 },
};

// app.js
const exportVar = require('./exportVar');
exportVar.printMsg();
