var img;

function preload() {
  img = loadImage("wolf.png");
}

function setup() {
  createCanvas(400, 400);
}

function draw() {
  background(220);
  image(img, 0, 0, 100, 100);
  
}