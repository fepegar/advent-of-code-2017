function Cell(i, j, w, h, value) {
  this.row = i;
  this.col = j;
  this.value = value;
  this.back = false;
  this.width = w;
  this.height = h;
  this.x = this.col * this.width + this.width/2;
  this.y = this.row * this.height + this.height/2;
  this.busy = false;
  this.direction = undefined;
  this.isLetter = isLetter(this.value);

  this.perpendicular = function() {
    if (this.value == VERTICAL) {
      return HORIZONTAL;
    }
    if (this.value == HORIZONTAL) {
      return VERTICAL;
    }
  }

  this.drawCell = function() {
    rectMode(CENTER);
    if (this.busy) {
      fill(255, 0, 0);
    } else {
      fill(30);
    }
    rect(this.x, this.y, this.width, this.height);
  }

  this.draw = function() {
    noStroke();
    this.drawCell();
    textSize(this.height);

    if (!this.value) {
      return;
    }
    if (this.isLetter) {
      fill(0, 255, 0);
      text(value, this.x, this.y);
    }
    if (this.value == '|' || this.value == '+') {
      fill(0, 255, 0, 100);
      rect(this.x, this.y, this.width / 5, this.height);
    }
    if (this.value == '-' || this.value == '+') {
      fill(0, 255, 0, 100);
      rect(this.x, this.y, this.width, this.height / 5);
    }

    if (this.busy) {
      ellipseMode(CENTER);
      fill(255, 0, 0);
      ellipse(this.x, this.y, this.width/2);
    }
  }

  this.checkNeighbors = function() {
    if (this.value != INTERSECTION) {  // go straight
      var nextRow = this.row + this.direction[0];
      var nextCol = this.col + this.direction[1];
      var next = grid[nextRow][nextCol];
      if (!next) {
        return undefined;
      }
      
      if (next.value == this.perpendicular()) {  // jump!
        steps += 1;
        nextRow += this.direction[0];
        nextCol += this.direction[1];
        next = grid[nextRow][nextCol];
      }

      if (next.isLetter) {
        letters.push(next.value);
        next.value = this.value;
        next.isLetter = false;
        next.direction = this.direction;
        return next;
      }

      if (next.value == INTERSECTION || this.value == next.value) {
        return next;
      }
    } else {  // intersection!
      var directions;
      if (horizontal(this.direction)) {
        directions = [down, up];
      } else {
        directions = [left, right];
      }
      for (var i = 0; i < directions.length; i++) {
        direction = directions[i];
        nextRow = this.row + direction[0];
        nextCol = this.col + direction[1];
        var row = grid[nextRow];
        if (!row) {
          continue;
        }
        next = row[nextCol];
        if (!next) {
          continue;
        }
        if (next.isLetter) {
          letters.push(next.value);
          if (horizontal(this.direction)) {
            next.value = VERTICAL;
          } else {
            next.value = HORIZONTAL;
          }
          next.direction = direction;
          next.isLetter = false;
          return next;
        } else if (vertical(next) && vertical(direction)) {
          this.direction = direction;
          return next;
        } else if (horizontal(next) && horizontal(direction)) {
          this.direction = direction;
          return next;
        }
      }
    }
    return undefined;
  }
}
