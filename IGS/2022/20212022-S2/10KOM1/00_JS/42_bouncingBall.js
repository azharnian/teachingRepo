<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Bouncing Ball</title>
</head>
<body>
	<canvas id="canvas" width="500" height="500" style="background-color: grey;"></canvas>
	<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
	<script type="text/javascript">
		let canvas = $('#canvas');
		let ctx = canvas[0].getContext('2d');

		function circle(x, y, radius, color, isFilled) {
			ctx.strokeStyle = color;
			ctx.beginPath();
			ctx.arc(x, y, radius, 0, 2*Math.PI, false);
			ctx.stroke();
			if (isFilled){
				ctx.fillStyle = color;
				ctx.fill();
			}
		}

		class Ball {

			constructor(x, y){
				this.x = x;
				this.y = y;
				this.color = "Red";
				this.radius = 5;

				this.xSpeed = 2;
				this.ySpeed = 3;
			}

			draw(){
				circle(this.x, this.y, this.radius, this.color, true);
			}

			move(){
				this.x += this.xSpeed;
				this.y += this.ySpeed;
			}

			checkCollisionEdge(){
				if (this.x < 0 || this.x > canvas[0].width){
					this.xSpeed = -this.xSpeed
				}
				if (this.y < 0 || this.y > canvas[0].height){
					this.ySpeed = -this.ySpeed
				}
			}
		}

		let ball = new Ball(250, 250);
		// ball.draw();

		let mainloop = setInterval( () => {
			ctx.clearRect(0, 0, canvas[0].width, canvas[0].height);

			ball.draw();
			ball.move();
			ball.checkCollisionEdge();
		}, 30)
	</script>
</body>
</html>