function setup() {
  createCanvas(500, 500);
}

function draw() {
  background(204);
  line(20, 50, 420, 110);

  triangle(347, 54, 392, 9, 200, 50); // (x1, y1, x2, y2, x3, y3)

  rect(180, 250, 220, 40); // (x1, y1, width, height)

  circle(412, 300, 50);  // (x1, y1, radius)

  ellipse(100, 300, 50, 100); // (x1, y1, width, height)

  arc(80, 80, 50, 50, radians(45), radians(315)); // (x1, y1, width, height, start, stop) *clockwise!
}