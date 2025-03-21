// The sum of the squares of the first ten natural numbers is,
// 1^2 + 2^2 + 3^2 ... + 10^2 = 385
//
//The square of the sum of the first ten natural numbers is,
// (1 + 2 + 3 ... + 10 = 55) => 55^2 = 3025
//
// Hence the difference between the sum of the squares of the first
// ten natural numbers and the square of the sum is 3025 - 385 = 2640.
//
// Find the difference between the sum of the squares of the first one
// hundred natural numbers and the square of the sum.

// sum of first x natural numbers
const sumOfNaturalsUpTo = function (num) {
  let sum = (num + 1) * (num / 2);
  return sum;
};

// long innefficient way
const sumOfSquaresOfNaturalsUpTo = function (num) {
  let sum = 0;
  for (let i = 1; i <= num; i++) {
    sum += i * i;
  }
  return sum;
};

console.log(
  sumOfNaturalsUpTo(100) * sumOfNaturalsUpTo(100) -
    sumOfSquaresOfNaturalsUpTo(100)
);

// optimized way to calculate sum of squares

//                  d = 0
//    a + b   + c + d = 1
//   8a + 4b + 2c + d = 5
//  27a + 9b + 3c + d = 14

// a = 1/3 , b = 1/2, c = 1/6
//sum = n/6 * (2n+1)*(n+1)

const sumOfSquaresOfNaturalsUpTo_optimized = function (num) {
  return (num * (2 * num + 1) * (num + 1)) / 6;
};

console.log(
  sumOfNaturalsUpTo(100) * sumOfNaturalsUpTo(100) -
    sumOfSquaresOfNaturalsUpTo_optimized(100)
);
