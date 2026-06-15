// ფუნქცია გამოიყენება იმისთვის რომ ერთი და იგივე კოდი მრავალჯერ გამოვიყენოთ და პროგრამა უფრო ორგანიზებული და მარტივი იყოს

// ფუნქციის შესაქმნელად გამოიყენება keyword function

function sum(a, b) {
    console.log(a + b);
}

sum(5, 3);

// return ფუნქციიდან აბრუნებს მნიშვნელობას


function checkNumber(num) {
    if (num > 10) {
        return true;
    } else {
        return false;
    }
}

console.log(checkNumber(15));
console.log(checkNumber(7));