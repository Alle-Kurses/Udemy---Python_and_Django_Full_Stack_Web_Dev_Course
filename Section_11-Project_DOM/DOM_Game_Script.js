/*function dataContent(){
	tData.addEventListener("click", function(){
	tData.textContent = "X";
})
}

tData = document.querySelectorAll("td");
tData.forEach(dataContent)*/

document.querySelectorAll('.table td')
.forEach(e => e.addEventListener("click", function() {
    //e.textContent = "X";
	if(e.innerHTML === ""){
		e.innerHTML = "X";
		return
	}
	if(e.innerHTML === "X"){
		e.innerHTML = "O";
		return
	}
	if(e.innerHTML === "O"){
		e.innerHTML = "";
		return
	}
}));

