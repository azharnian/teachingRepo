let counter = 0;
// function count() { //arrowFunction (lambda di python)
let count = () => {
	counter++;
	// document.querySelector("#counter").innerHTML = counter;
	$('#counter').text(counter);
	if (counter % 10 === 0){
		alert(`Counter is at ${counter} !.`);
	}
}