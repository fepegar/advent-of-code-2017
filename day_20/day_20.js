/*
 * Solutions for day 20.
 */

var particles;

function setup() {
  createCanvas(windowWidth, windowHeight);
  particles = readParticles(particlesList);
  frameRate();
}

function draw() {
  colorMode(RGB);
  background(0, 30, 0);

  translate(width/2, height/2);

  noStroke();
  fill(255, 50);
  ellipse(0, 0, 20);

  for (var i = 0; i < particles.length; i++) {
    particles[i].update();
    particles[i].draw();
  }
  var closest = getClosestToCenter();
  console.log("Closest:", closest)//, particles[closest].p.z);
}


function getClosestToCenter() {
  minDist = Number.MAX_SAFE_INTEGER;
  var d;
  var closest;
  for (var i = 0; i < particles.length; i++) {
    d = particles[i].distanceToCenter();
    if (d < minDist) {
      minDist = d;
      closest = i;
    }
  }
  return closest;
}
