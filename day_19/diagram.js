var VERTICAL = '|';
var HORIZONTAL = '-';
var INTERSECTION = '+';
var down = [1, 0];
var up = [-1, 0];
var left = [0, -1];
var right = [0, 1];
var steps = 0;
var letters = [];

function Diagram(string) {
  var lines = string.split('\n');
  var nLines = lines.length;
  this.lines = lines.slice(1, nLines-1);
  this.rows = this.lines.length;
  this.current = undefined;
  this.stack = [];
  this.moving = true;

  this.getNumberOfColumns = function() {
    var maxCols = -1;
    for (var i = 0; i < this.rows; i++) {
      maxCols = max(maxCols, this.lines[i].length);
    }
    return maxCols;
  }

  this.cols = this.getNumberOfColumns();
  var cellHeight = height / this.rows;
  var cellWidth = width / this.cols;

  var value;
  for (var row = 0; row < this.rows; row++) {
    grid.push([])
    for (var col = 0; col < this.cols; col++) {
      value = this.lines[row][col];
      grid[row].push(new Cell(row, col, cellWidth, cellHeight, value));
    }
  }

  this.draw = function() {
    this.current.draw();
  }

  this.drawGrid = function() {
    textAlign(CENTER, CENTER);
    for (var row = 0; row < this.rows; row++) {
      for (var col = 0; col < this.cols; col++) {
        grid[row][col].draw()
      }
    }
  }

  this.findFirst = function() {
    var firstLine = grid[0];
    var firstCell;
    for (var col = 0; col < firstLine.length; col++) {
      if (firstLine[col].value == VERTICAL) {
        this.current = grid[0][col];
        break;
      }
    }

    // this.current = grid[74][95]; ///////////////
    this.current.direction = down;
    this.current.busy = true;
    this.current.visited = true;
  }

  this.move = function() {
    if (!this.moving) {return};
    var next = this.current.checkNeighbors()
    if (next) {
      this.setNext(next);
    } else {
      print('No neighbors found')
      steps += 1;
      this.moving = false;
    }
  }

  this.setNext = function(next) {
    this.current.busy = false;
    next.busy = true;
    if (!next.direction) {
      next.direction = this.current.direction;
    }
    this.current = next;
    if (next.isLetter) {
      var letter = next.value
      print(letter)
      letters.push(letter);
    }
    steps += 1;
  }
}

function isLetter(str) {
  if (!str) {
    return false;
  }
  return str.length === 1 && str.match(/[A-Z]/i);
}


function opposite(direction) {
  if (direction == down) {
    return up;
  } else if (direction == up) {
    return down;
  } else if (direction == left) {
    return right;
  } else if (direction == right) {
    return left;
  }
}

function horizontal(thing) {
  if (thing.constructor === Array) {
    return thing[0] == 0;
  } else {
    return thing.value == HORIZONTAL;
  }
}

function vertical(thing) {
  if (thing.constructor === Array) {
    return thing[1] == 0;
  } else {
    return thing.value == VERTICAL;
  }
}
