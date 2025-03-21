//The prime factors of 13195 are 5, 7, 13 and 29.
//What is the largest prime factor of the number 600851475143 ?

//prime numbers


//check if n is prime
function isprime(n) {
    for (let i = 2 ; i < n; i++) {
        if (n % i===0) {return false}
    }
    return true
}

let num = 600851475143
let prime_factors = []
for (let k=1 ; k<num; k+=2){
    if (isprime(k) && (num%k ===0)){
        prime_factors.push(k) 
        prime_factors.push(num/k) 
        console.log(prime_factors)
        num = num/k
    } 
}
console.log(prime_factors) 
console.log(prime_factors[prime_factors.length-1]) 