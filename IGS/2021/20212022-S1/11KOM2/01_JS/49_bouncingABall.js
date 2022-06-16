<!DOCTYPE html>
<html>
<head>
	<title>Bouncing A Ball</title>
</head>
<body>
	<canvas id="canvas" width="500" height="500" style="border: 1px solid black"></canvas>
	<script type="text/javascript">
		
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
				this.x = 250;
				this.y = 250;
				this.color = "red";
				this.radius = 5;

				this.xSpeed = -2;
				this.ySpeed = 3;
			}

			draw(){
				circle(this.x, this.y, this.radius, this.color, true);
			}

			move(){
				this.x += this.xSpeed;
				this.y += this.ySpeed;
			}

			checkCollision(){
				if (this.x < 0 || this.x > 500){
					this.xSpeed = -this.xSpeed;
				}

				if (this.y < 0 || this.y > 500){
					this.ySpeed = -this.ySpeed;
				}
			}
		}

		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let ball = new Ball()

		setInterval( () => {
			ctx.clearRect(0, 0, 500, 500);

			ball.draw();
			ball.move();
			ball.checkCollision();
		}, 30)

	</script>
</body>
</html>