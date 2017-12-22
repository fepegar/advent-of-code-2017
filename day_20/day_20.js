/*
 * Solutions for day 20.
 */

var particles;
var part = 2;

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

  if (part == 2) {
    collide();
  }

  for (var i = 0; i < particles.length; i++) {
    particles[i].update();
    particles[i].draw();
  }
  var closest = getClosestToCenter();
  if (part == 1) {
    console.log("Closest:", closest);
  } else if (part == 2) {
    console.log("Particles:", particles.length);
  }
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


function collide() {
  var destroy = new Set();
  var particle1;
  var particle2;
  for (var i = 0; i < particles.length - 1; i++) {
    particle1 = particles[i];
    for (var j = i+1; j < particles.length; j++) {
      particle2 = particles[j];
      if (particle1.p.dist(particle2.p) < 0.0001) {
        destroy.add(particle1);
        destroy.add(particle2);
      }
    }
  }

  var index;
  for (let particle of destroy) {
    index = particles.indexOf(particle);
    particles.splice(index, 1);
  }
}
