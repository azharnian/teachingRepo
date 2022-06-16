var img;

function setup() {
  createCanvas(400, 400);
  img = loadImage("wolf.png");
}

function draw() {
  background(220);
  image(img, 0, 0, 100, 100);
  
}