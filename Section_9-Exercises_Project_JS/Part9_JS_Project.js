var firstName = prompt("Enter your First Name: ").toLowerCase();
var lastName = prompt("Enter your Last Name: ").toLowerCase();
var age = prompt("Enter your age: ");
var height = prompt("Enter your height: ");
var pet = prompt("What is your pet's name?");

if(firstName[0] === lastName[0] && age >= 20 && age <= 30 && height >= 170 && pet[pet.length-1] === "y"){
	console.log("Welcome Comrade! You've passed the Spy Test.")
}else{
	console.log("Sorry, nothing to see here.")
}