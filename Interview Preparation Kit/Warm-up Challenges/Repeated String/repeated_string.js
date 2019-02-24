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

// Complete the repeatedString function below.
function repeatedString(s, n) {
    const regex = /a/g;
    const baseMatch = s.match(regex) || [];
    const fullStringMatch = baseMatch.length * Math.floor(n / s.length);
    let partialStringMatch = 0;
    if (n % s.length !== 0) {
        const match = s.slice(0, n % s.length).match(regex);
        if (match) {
            partialStringMatch = s.slice(0, n % s.length).match(regex).length;
        }
    }
    return fullStringMatch + partialStringMatch;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const s = readLine();

    const n = parseInt(readLine(), 10);

    let result = repeatedString(s, n);

    ws.write(result + "\n");

    ws.end();
}
