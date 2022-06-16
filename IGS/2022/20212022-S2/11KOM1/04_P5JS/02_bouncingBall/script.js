

class Ball {

	constructor(x, y){
		this.x = x;
		this.y = y;
		this.radius = 20;

		this.xSpeed = Math.ceil(Math.random() * 5);
		this.ySpeed = Math.ceil(Math.random() * 5);
	}

	draw(){
		noStroke();
		fill(255, 0, 0);
		ellipse(this.x, this.y, this.radius, this.radius);
	}

	move(){
		this.x += this.xSpeed;
		this.y += this.ySpeed;
	}

	checkCollisionWithEdge(){
		if (this.x < 0 || this.x > 500) this.xSpeed = -this.xSpeed;
		if (this.y < 0 || this.y > 500) this.ySpeed = -this.ySpeed;
	}
}

let ball = new Ball(250, 250);

function setup() {
	createCanvas(500, 500);
	frameRate(24);
}

function draw() {

	clear();
	background(120);
	ball.draw();
	ball.move();
	ball.checkCollisionWithEdge();

}