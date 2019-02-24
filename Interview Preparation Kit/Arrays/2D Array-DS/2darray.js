'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function getHourglass(arr, i, j) {
    let hourglass = 0;
    for (var x = i; x - i < 3; x++) {
        for (var y = j; y - j < 3; y++) {
            if (x - i === 1 && (y - j === 0 || y - j == 2)) {
                continue;
            }
            hourglass += arr[x][y];
        }
    }
    return hourglass;
}

// Complete the hourglassSum function below.
function hourglassSum(arr) {
    let totalTime = [];
    for (var i = 0; i < 4; i++) {
        for (var j = 0; j < 4; j++) {
            totalTime.push(getHourglass(arr, i, j));
        }
    }
    return totalTime.sort((a, b) => b - a)[0];
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    let arr = Array(6);

    for (let i = 0; i < 6; i++) {
        arr[i] = readLine().split(' ').map(arrTemp => parseInt(arrTemp, 10));
    }

    let result = hourglassSum(arr);

    ws.write(result + "\n");

    ws.end();
}
