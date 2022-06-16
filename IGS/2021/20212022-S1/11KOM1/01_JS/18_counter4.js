document.addEventListener('DOMContentLoaded', function (){
	document.querySelector('button').onclick = count;
});

let counter = 0;
var count = function () {
	counter++;
	document.querySelector('#counter').innerHTML = counter;

	if (counter % 10 === 0) {
		alert(`Counter is at ${counter}!`);
		//alert('Counter is at '+counter+"!");
	}
};