const numbers = [2, 5, 7, 8, 9, 12, 15]

numbers.forEach((number, index) => {
    if (number % 2 !== 0 && index % 2 !== 0) {
        console.log(number)
    }
})
