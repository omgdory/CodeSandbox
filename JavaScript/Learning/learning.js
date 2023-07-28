// console.log('Hi -from main.js')

// test comment
// const Person = {
//     'meritLevel': 5,
//     'hours': 7,
// }

// const primeNumbers = [1, 2, 3, 5, 7, 11]


// let x = 10
// let y = 5
// //console.log(x > y)

// const isValidNumber = x > 100 && y < 8
//console.log(isValidNumber)

// x = 11
// const isEven = x % 2 == 0 ? true : false
// console.log(isEven)

// Explicit Conversions
// console.log(String(25))
// console.log((500).toString())
// console.log(Boolean(10))

// Equality
// const var1 = 10
// const var2 = '10'

// console.log(var1 == var2) // will be true
// console.log(var1 === var2) // will be false (different types)


// Conditionals
// const num = -20
// if(num > 0) {
//     console.log(num + ' is positive')
// } else if(num == 0) {
//     console.log(num + ' is zero')
// } else {
//     console.log(num + ' is negative')
// }

// const color = 'dag'
// switch(color) {
//     case 'red':
//         console.log('FF0000')
//         break
//     case 'blue':
//         console.log('0000FF')
//         break
//     case 'green':
//         console.log('00FF00')
//         break
//     default:
//         console.log('No existing color')
//         break
// }

// let primes = [2, 3, 5, 7, 11, 13]
// let sum = 0
// for(let i=0; i<primes.length; i++) {
//     sum += primes[i]
// }
// let ave = sum/primes.length

// console.log(sum)
// console.log(sum + '/' + primes.length + ' = ' + ave)

// const numArr = [7,10,100,20,50]
// for(const num of numArr) {
//     console.log(num)
// }

// Functions
function firstFunction() {
    console.log('Hello world')
}

// function fact(n) {
//     if (n == 0 || n == 1) {
//         return 1
//     }
//     return n *= fact(n - 1)
// }

// Arrow functions
// const arrowSum = (a, b) => a + b
// const swag = a => a + 5
// const sum1 = arrowSum(2, 5) // 7
// const sum2 = swag(3) // 8
// console.log(sum1)
// console.log(sum2)

firstFunction()

// Objects
const name = "Tyson"
const meritLevel = 10

const person = {
    name,
    meritLevel,
    om: false,
};
// console.log(person.name + ' of Merit ' + person.meritLevel)
// Tyson of Merit 10

// copying objects but changing specific attributes
// const person2 = {...person, name: "Lawd"}
// console.log(person2.name + ' of Merit ' + person.meritLevel)

// let names = ["Pedro", "Jessica", "Carol"]
// let swag = names.map((names) => {return names+'Z'})
// for(let i=0; i<swag.length; i++) {
//     console.log(swag[i])
// }

// // Consider...
// let names2 = ["Pedro", "Jessica", "Meritman", "Pedro", "Pedro"]
// let testing = names2.filter((name) => {
//     return name !== "Pedro"
// });
// for(let i=0; i<testing.length; i++) {
//     console.log(testing[i])
// }


