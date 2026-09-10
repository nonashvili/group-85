let checkNumber = function(number) {
    return number > 0 && number % 2 == 0 ? "Positive Even"
        : number > 0 && number % 2 != 0 ? "Positive Odd"
        : number < 0 && number % 2 == 0 ? "Negative Even"
        : number < 0 && number % 2 != 0 ? "Negative Odd"
        : number == 0 ? "Zero"
        : "Wrong Number"
}

console.log(checkNumber(20))
