<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Car Object</title>
</head>
<body>
	<!-- Jquery Lib -->
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<!-- end Jquery -->
	<script type="text/javascript">

		// function draw(){
		// 	let carImg = '<img src="car.png">';

		// 	this.carElement = $(carImg);

		// 	this.carElement.css({
		// 		position : "absolute",
		// 		left : this.x,
		// 		top : this.y
		// 	})

		// 	$('body').append(this.carElement);
		// }
		
		// constructor

		let Car = function (x, y) {
			this.x = x;
			this.y = y;
			this.odometer = 0;

			this.show = function () {
				let carImg = '<img src="car.png">';

				this.carElement = $(carImg);

				this.carElement.css({
					position : "absolute",
					left : this.x,
					top : this.y
				})

				$('body').append(this.carElement);
			}

			this.show = draw;
		}

		Car.prototype.readOdometer = function (){
			console.log(`Car : ${this.odometer} miles`);
		}

		let toyota = new Car(10, 20);
		toyota.show();
		toyota.readOdometer();

		let tesla = new Car(100, 200);
		tesla.show();

	</script>
</body>
</html>