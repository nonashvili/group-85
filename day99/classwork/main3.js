let numbers = [12, 25, 48, 101, 77, 120, 33, 200, 15]

for (let number of numbers) {
    if (number % 2 === 0 || number > 100) {
        console.log(number)
    }
}
