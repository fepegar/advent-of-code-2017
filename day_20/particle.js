function Particle(line) {
  var properties = matchLine(line);
  this.p = properties[0];
  this.v = properties[1];
  this.a = properties[2];

  colorMode(HSB);
  this.color = color(random(255), random(80, 100), random(80, 100));

  this.update = function() {
    this.v.add(this.a);
    this.p.add(this.v);
  }

  this.draw = function() {
    noStroke();
    colorMode(HSB);
    fill(this.color);
    ellipse(this.p.x, this.p.y, 5);
  }

  this.distanceToCenter = function() {
    return abs(this.p.x) + abs(this.p.y) + abs(this.p.z);
  }
}


function matchLine(line) {
  var numbers = line.match(/-?\d+/g);
  for (var i = 0; i < numbers.length; i++) {
    numbers[i] = parseFloat(numbers[i]);
  }
  var p = createVector(numbers[0], numbers[1], numbers[2]);
  var v = createVector(numbers[3], numbers[4], numbers[5]);
  var a = createVector(numbers[6], numbers[7], numbers[8]);
  var scale = 10000;
  p.div(scale);
  v.div(scale);
  a.div(scale);
  return [p, v, a];
}


function readParticles(string) {
  var lines = string.split('\n');
  lines = lines.slice(1, lines.length-1);
  array = [];
  for (var i = 0; i < lines.length; i++) {
    array.push(new Particle(lines[i]));
  }
  return array;
}
