
var firewall;

function setup() {
  createCanvas(400, 400);
  firewall = Firewall(example);
}

function draw() {
  background(220);
}

function Firewall(dict) {
  for (var i = 0; i < dict.length; i++) {

  }
}

DOWN = 1;
UP = -1;

function Layer(number, range, x) {
  this.number = number;
  this.range = range;
  this.x = x;
  this.y = 10;
  this.scanner = 0;
  this.direction = DOWN;
  this.packet = false;

  this.show = function() {
    text(this.number, this.x, this.y)
  }
}
