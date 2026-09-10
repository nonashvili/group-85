let strings = ["hello", "zaza", "world", "sun", "car"]

let numbers = [2, 4, 6, 2335, 2]

let newArray = strings.concat(numbers)

newArray.push(true)
newArray.shift()

let newArray2 = newArray.slice(3, 7)

console.log(newArray2)
console.log(Array.isArray(newArray2))