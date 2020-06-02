var answer = prompt("Would you like to start the roster web app? y/n");
var idk = true;
var holder = [];

if(answer === "y"){
	while(idk === true){
		while(true){
			var answer2 = prompt("Please select an action: add, remove, display, or quit.");
			
			if(answer2 === "add"){
				holder.push(prompt("What name would you like to add?"));
			}
			else if(answer2 === "remove"){
				holder.splice(holder.indexOf(prompt("What name would you like to remove")), 1);
			}
			else if(answer2 === "display"){
				console.log(holder);
			}
			else if(answer2 === "quit"){
				idk = false;
				break;
			}
			else{
				continue;
			}
		}
	}
}

alert("Thanks for using the Web App! Please refresh the page to start over.");
