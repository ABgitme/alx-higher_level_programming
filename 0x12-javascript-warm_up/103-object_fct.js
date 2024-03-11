#!/usr/bin/node
const myObject = {
  type: 'object',
  value: 12,
  /**
    * Increments the value property of the object.
    */
  incr: function () {
    this.value++; // Increment the value property of the object
  }
};
console.log(myObject);

myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
myObject.incr();
console.log(myObject);
