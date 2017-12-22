/*
 * Solutions for day 19.
 */

var diagram;
var grid = [];

function setup() {
  createCanvas(windowHeight, windowHeight);
  diagram = new Diagram(inputDiagram);
  diagram.findFirst();
  background(30);
  diagram.drawGrid();
}

function draw() {
  diagram.move();
  diagram.draw();
}
