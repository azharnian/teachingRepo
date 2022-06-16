// document.addEventListener('DOMContentLoaded', listenClick);

// function listenClick(){
// 	document.querySelector("button").onclick = count;
// }

document.addEventListener('DOMContentLoaded', function (){
	document.querySelector("button").onclick = count;
});

let counter = 0;
function count() {
	counter++;
	document.querySelector("#counter").innerHTML = counter;

	if (counter % 10 === 0){
		alert(`Counter is at ${counter} !`) //backtick
		//alert("Counter is at "+counter+" !");
	}
}