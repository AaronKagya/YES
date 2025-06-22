/**
 * IF STATEMENTS
 */
//SYNTAX
// if (condition) {
//        logic
//}else if (condition){
//      logic
//}else{
//      logic
// }

//age, child , adult, invalid

let age = 0;
if (age<0){
    console.log("age cannot be negative")
}else if (age>=18){
    console.log("this is an Adult")
}else
    console.log("this is a child")


// find a day by inputing a no. in the system,

 let number = 7;
 switch(number){
    case 1:
        console.log("This is Sunday")
        break; 
    case 2:
        console.log("This is a Monday")
        break;
    case 3:
        console.log("This is a Tuesday")
        break;
    case 4:
        console.log("This is a Wednesday")
        
    case 5:
        console.log("This is a Thursday")
        break;
    case 6:
        console.log("This is a Friday")
        break;
    case 7:
        console.log("This is a Saturday")
        break;    
    default:
        console.log("This day does not exist")
        break;
 }

 /**
  * LOOPS
  */
 // FOR LOOPS
//for (inntialization, condition, increment){
//      results
//}
// print the 100 counting numbers.

for (let i=1; i<=100; i+=1 ){
    console.log(i);
}

//while loop 
// intiliazation

//while (condition){
//results
//increment
//}
let i = 1;
while (i <= 100) {
    console.log(i);
    i+=1;
}

//for in loop //Arrays
let fruitList = ["apples" , "mangoes",'oranges']
for (fruit in fruitLists){
    console.log(fruitList[fruit]);
}

//for of loop
for (fruit of fruitList){
    console.log(fruit);
    
}