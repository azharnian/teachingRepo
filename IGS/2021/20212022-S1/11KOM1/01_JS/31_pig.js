<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Object</title>
</head>
<body>
	<script type="text/javascript">

	function sleep() {
		console.log("Zzzzzzzzzz");
	}
		
	let dog = {
		name : "Pancake",
		legs : 4,
		isAwesome : true,
		sleep : sleep,

		eat : function () {
			console.log(`${this.name} is still eating ... , sorry!`); // self. referencing attribute to object
		}
	}

	dog.bark = function (){
		console.log(`Woof woof!!!, my name is ${this.name} !`)
	}



	console.log(dog.name);
	console.log(dog['legs']);
	dog.bark();
	dog.sleep();
	dog.eat();


	</script>
</body>
</html>