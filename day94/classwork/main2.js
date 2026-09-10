let checkName = name => {
    if(name.startsWith("ს")) {
        return "Good Name"
    } else {
        return "Still Good Name"
    }
}

console.log(checkName("საბა"))
console.log(checkName("ზვიადი"))