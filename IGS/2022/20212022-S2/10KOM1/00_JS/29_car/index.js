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

		//constructor
		class Car {

			constructor (x, y) {
				this.x = x;
				this.y = y;
				this.speed = 1;
				this.odometer = 0;
			}

			show() {
				let carImg = '<img src="car.png">';

				this.carElement = $(carImg);

				this.carElement.css({
					position : "absolute",
					left : this.x,
					top : this.y
				})

				$("body").append(this.carElement);
			}
			moveRight(){
				this.x += this.speed;

				this.carElement.css({
					left: this.x
				})
				this.odometer += this.speed;
			}

			moveLeft(){
				this.x -= this.speed;

				this.carElement.css({
					left: this.x
				})

				this.odometer += this.speed;
			}


			moveUp(){
				this.y -= this.speed;

				this.carElement.css({
					top: this.y
				})

				this.odometer += this.speed;
			}

			moveDown(){
				this.y += this.speed;

				this.carElement.css({
					top: this.y
				})

				this.odometer += this.speed;
			}


		}

		Car.prototype.readOdometer = function (){
			console.log(`Car : ${this.odometer} miles`);
		}

		let toyota = new Car(10, 20);
		toyota.show();
		// toyota.moveRight();
		// toyota.moveDown();
		// toyota.moveDown();
		// toyota.moveRight();
		toyota.readOdometer();

		let tesla = new Car(100, 200);
		tesla.show();

		function run() {
			tesla.moveRight();
			if (tesla.x > 1400){
				tesla.x = -300;
			}
		}

		let mainloop = setInterval(run, 5);

	</script>
</body>
</html>