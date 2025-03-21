// A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

// Find the largest palindrome made from the product of two 3-digit numbers.

// 999* 999 = 998,001 upper bound
// 100* 100 = 10,000 lower bound

// // create array of palindrome numbers
let LargestPalindrome = 0;
ispalindrome = function (num) {
  numStr = num.toString();
  reversed = numStr.split("").reverse().join("");
  if (numStr === reversed) {
    // console.log(numStr);
    return true;
  }
};

for (let i = 999; i > 100; i--) {
  for (let k = 999; k > i; k--) {
    // k always larger than i
    let num = i * k;
    if (ispalindrome(num) && num > LargestPalindrome) {
      LargestPalindrome = num;
    }
  }
}

console.log(LargestPalindrome);

// console.log(palindrome_array[500]);
// const factors = function (num) {};
