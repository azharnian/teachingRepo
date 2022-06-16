<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>Making Thing Move</title>
</head>
<body>
	<canvas id="canvas" width="400" height="400" style="background-color: grey;"></canvas>
	<script type="text/javascript">
			
		let canvas = document.getElementById("canvas");
		let ctx = canvas.getContext("2d");

		let squareObject = {
			positionX : 0,
			positionY : 0,
			direction : 1,
			color : "Black",
			size : 20,
			showSquare : function () {
				ctx.fillStyle = this.color;
				ctx.fillRect(this.positionX, this.positionY, this.size, this.size);
			},
			changeColor : function (newColor) {
				this.color = newColor
			},
			isTouchRightEdges : function () {
				if (this.positionX > canvas.width){
					return true
				}
			},
			isTouchLeftEdges : function () {
				if (this.positionX < 0){
					return true
				}
			},
			changeDirectionAndColor : function (){
				if (this.isTouchRightEdges()){
					this.direction = -1;
					this.color = "White"
				} else if (this.isTouchLeftEdges()){
					this.direction = 1;
					this.color = "Black"
				}

			},
			horizontalMove : function (){
				this.positionX += (this.direction * 1);
			}

		}

		setInterval( () => {
			ctx.clearRect(0, 0, canvas.width, canvas.height);
			squareObject.showSquare();
			squareObject.horizontalMove();
			squareObject.changeDirectionAndColor();
		}, 10);

		

	</script>
</body>
</html>