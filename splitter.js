let parts = msg.payload.split(',');

let temp = parts[0].split(':')[1];
let hum = parts[1].split(':')[1];

return [
    { payload: parseInt(temp) }, // Output 1: Temp
    { payload: parseInt(hum) }   // Output 2: Hum
];