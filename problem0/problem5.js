// 2520 is the smallest number that can be divided by each
// of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly
// divisible by all of the numbers from 1 to 20?

//1*2*3...*19*20 = 2.432902e+18 --> 2,000,000,000,000,000,000

// 20 = 2*10
// 19
// 18 = 6*3
// 17
// 16 = 8*2
// 15 = 5*3
// 14 = 7*2
// 13
// 12 = 4*3
// 11

// prime numbers between 1-20 = 2, 3, 5, 7, 11, 13, 17, 19

// prime factorization of 2520 = 2 x 2 x 2 x 3 x 3 x 5 x 7

const isPrime = function (num) {
  if (num === 2) {
    return true;
  } else {
    for (let i = 2; i < num; i++) {
      if (num % i === 0) {
        return false;
      }
    }
    return true;
  }
};

//get primes up to *number*
const primesUpTo = function (num) {
  const factorsArray = [];
  for (let factor = 2; factor <= num; factor++) {
    if (isPrime(factor)) {
      factorsArray.push(factor);
    }
  }
  return factorsArray;
};

// prime factoriziation of any number
const primeFactors = function (num) {
  let resultsArray = [];
  for (let i = 0; i < primes.length; i++) {
    factor = primes[i];
    while (num % factor === 0 && factor < num) {
      resultsArray.push(factor);
      num = num / factor;
    }
  }
  resultsArray.push(num);
  return resultsArray;
};

// given minimum prime, check for non-prime factors
const smallestMultiple = function (maxFactor) {
  const primes = primesUpTo(maxFactor);
  //minimum result is product of all primes
  let result = primes.reduce(
    (previousValue, currentValue) => previousValue * currentValue,
    1
  );
  for (let factor = 1; factor <= maxFactor; factor++) {
    if (result % factor === 0) {
      console.log(factor + " is already factor");
    } else {
      // factor is not prime and not already include
      console.log(factor + " is not yet a factor");
      const primeFactorsofFactor = primeFactors(factor);
      result = result * primeFactorsofFactor[primeFactorsofFactor.length - 1];
    }
  }
  return result;
};

console.log(smallestMultiple(20));
