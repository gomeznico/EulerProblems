// Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
//By starting with 1 and 2, the first 10 terms will be:

// 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

// By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
// find the sum of the even-valued terms.

// recursive fibonacci sequence
function fibonacci(i){
    if (i === 1) {return 1}
    else if (i === 2) {return 2}
    else {return fibonacci(i-1)+fibonacci(i-2)}   
}

let sum = 0
let f_sequence = [1]
let even_f =[]
while (f_sequence[f_sequence.length-1] < 4000000) {
    next_number =fibonacci(f_sequence.length+1)
    f_sequence.push(next_number)
    if (next_number%2 === 0) {
        sum += next_number
        even_f.push(next_number)
    }
}
console.log(sum)

// console.log(fibonacci(1))
// console.log(fibonacci(12))


//-------------------//
//Euler solution:

// let sum = 0
// let limit=4000000
// let a=1
// let b=1
// while (b<limit) {
//     if (b&2 == 0) {sum += b}
//     let h = a+b
//     let a=b
//     let b=h
// }
// console.log(sum)