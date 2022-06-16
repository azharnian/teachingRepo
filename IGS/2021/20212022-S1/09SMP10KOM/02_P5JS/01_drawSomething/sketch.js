function setup() {
  // put setup code here
  createCanvas(480, 120);
}

function draw() {
  // put drawing code here
  /**
  background(204);
  ellipse(50, 50, 80, 80);
  **/
  if (mouseIsPressed) {
    fill(0);
  } else {
    fill(255);
  }
  ellipse(mouseX, mouseY, 80, 80);
}