let numbers = [15, 8, 42, 8, 31, 42, 19, 8]

numbers[numbers.indexOf(8)] = 80
numbers[numbers.indexOf(42)] = 420
numbers[numbers.lastIndexOf(8)] = 800

numbers[1] += 5;

console.log(numbers)
