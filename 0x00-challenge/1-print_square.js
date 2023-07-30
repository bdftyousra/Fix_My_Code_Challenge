#!/usr/bin/env node

function printSquare(size) {
    for (var i = 0; i < size; i++) {
        for (var j = 0; j < size; j++) { // <-- Fixed the condition here
            process.stdout.write('#');
        }
        console.log('');
    }
}

if (process.argv.length !== 3) {
    console.log('Usage: ./1-print_square.js <size>');
    process.exit(1);
}

var size = parseInt(process.argv[2]);
printSquare(size);

