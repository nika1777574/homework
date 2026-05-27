
let number = 10;

if (number % 2 === 0) {
    console.log("even");
} else {
    console.log("odd");
}

let number2 = 15;

if (number2 % 3 === 0 && number2 % 5 === 0) {
    console.log("ეს რიცხვი არის 3 ის და 5 ის ჯერადი");
} 
else if (number2 % 3 === 0 || number2 % 5 === 0) {
    console.log("ეს რიცხვი არის სამის ან ხუთის ჯერადი");
} 
else {
    console.log("ეს რიცხვი არ არის არც სამის და არც ხუთის ჯერადი");
}

// == 
console.log(5 == "5");

// === 
console.log(5 === "5"); 

// != 
console.log(5 != 3); 

// !== 
console.log(5 !== "5"); 

// >
console.log(10 > 5);

// < 
console.log(3 < 7); 

// >= 
console.log(5 >= 5); 

// <= 
console.log(4 <= 9);