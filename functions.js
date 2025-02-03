// // two types,

// - void function
// - returning function

// returning function
function addition(numberOne, numberTwo) {
    return numberOne + numberTwo;

}
//void function
function sum(numberOne, numberTwo) {
    let summation = numberOne + numberTwo;
    console.log(summation);
}


sum(8, 6)
console.log(addition(32, 67));


//arrow funtions
const subtraction = (numberOne, numberTwo) => {
    return numberOne - numberTwo
}
//void function
const difference = (numberOne, numberTwo) => {
    console.log('the difference is ${numberOne - numberTwo}');

}

//calling the functions
console.log(subtraction(67, 32));
difference(99, 67);


//default parameters
const Welcome = (username) => {
    console.log("Welcome back ${username}");

}