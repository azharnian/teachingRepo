<!DOCTYPE html>
<html>
<head>
	<title>Controlling Ball</title>
</head>
<body>
	<canvas id="canvas" width="500" height="500" style="border: 1px solid black"></canvas>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script type="text/javascript">
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let circle = function (x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, true);
			ctx.stroke();
			if (isFilled){
				ctx.fillStyle = color;
				ctx.fill();
			}
		}
		
		class Ball {
			constructor(){
				this.x = canvas.width/2;
				this.y = canvas.height/2;
				this.color = "blue";
				this.radius = 5;

				this.speed = 5

				this.xSpeed = 0;
				this.ySpeed = 0;
			}

			draw(){
				circle(this.x, this.y, this.radius, this.color, true);
			}

			move(){
				this.x += this.xSpeed;
				this.y += this.ySpeed;

				if (this.x < 0) {
					this.x = canvas.width;
				} else if (this.x > canvas.width){
					this.x = 0
				} else if (this.y < 0) {
					this.y = canvas.height;
				} else if (this.y > canvas.height){
					this.y = 0
				}
			}

			checkCollision(){
				if (this.x < 0 || this.x > 500){
					this.xSpeed = -this.xSpeed;
				}

				if (this.y < 0 || this.y > 500){
					this.ySpeed = -this.ySpeed;
				}
			}

			setDirection(direction){
				if (direction === "up"){
					this.xSpeed = 0;
					this.ySpeed = -this.speed;
				}
				if (direction === "down"){
					this.xSpeed = 0;
					this.ySpeed = this.speed;
				}
				if (direction === "left"){
					this.xSpeed = -this.speed;
					this.ySpeed = 0;
				}
				if (direction === "right"){
					this.xSpeed = this.speed;
					this.ySpeed = 0;
				}
				if (direction === "stop"){
					this.xSpeed = 0;
					this.ySpeed = 0;
				}
			}


		}
		let ball = new Ball();

		let keyNames = {
			32 : "stop",
			37 : "left",
			38 : "up",
			39 : "right",
			40 : "down"
		}

		$("body").keydown( event => {
			let direction = keyNames[event.keyCode];
			ball.setDirection(direction);
		})

		setInterval(()=> {
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			ball.draw();
			ball.move();
			// ball.checkCollision();
		}, 30);
	</script>
</body>
</html>