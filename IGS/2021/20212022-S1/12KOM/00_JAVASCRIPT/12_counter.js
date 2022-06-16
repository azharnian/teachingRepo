let counter = 0;
var count = function (){
	counter++;
	document.querySelector('#counter').innerHTML = counter;

	if (counter%10 === 0){
		alert(`Counter is at ${counter}!`) //backtick, fitur js versi es6
		//alert("Counter is at "+counter+"!")
	}
}