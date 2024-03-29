#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if ((w > 0 && h > 0) && (Number.isInteger(w) && Number.isInteger(h))) {
      this.width = w;
      this.height = h;
    }
  }

  rotate () {
    // Exchange width and height
    const temp = this.width;
    this.width = this.height;
    this.height = temp;
  }

  double () {
    // Multiply width and height by 2
    this.width *= 2;
    this.height *= 2;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += 'X';
      }
      console.log(row);
    }
  }
}
module.exports = Rectangle;
