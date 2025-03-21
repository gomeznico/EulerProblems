//If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
//The sum of these multiples is 23.
//Find the sum of all the multiples of 3 or 5 below 1000.

// slow way below, O(2n)

let limit = 999
let sum = 0
for (let i = 0; i <=limit; i++) {
 if (i%3 ===0 || i%5===0) {sum = sum+i}   
}
console.log(sum)  //total = 233168



//clever way below, O(1)

function SumDivisibleBy(n,target) {
    p = Math.floor(target/n)
    let sum = Math.floor(n*(1/2)*(p)*(p+1))
    return sum
}

//if target is some very large like 
//sum of 1+2+3+4...+n =  1/2 * n * (n+1) 
//(3 + 6 + 9 + 12 + ... +999) = 3*(1+2+3+4...+ (999/3)) = 3* (1/2 * target/3 * (target/3 + 1))
console.log(SumDivisibleBy(3,999))
console.log(SumDivisibleBy(5,999))
console.log(SumDivisibleBy(15,999))
total = SumDivisibleBy(3,999) + SumDivisibleBy(5,999) - SumDivisibleBy(15,999) 
console.log(total) //234168

