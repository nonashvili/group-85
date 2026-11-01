let company = {
    name: "TechVision",
    employees: 45,
    founded: 2015,
    city: "Tbilisi",
    departments: 4,
    budget: 120000,
    active: true,
    projects: 8
}
let newList = Object.keys(company)
let newList1 = Object.values(company)

console.log(newList)
console.log(newList1)

for (let i = 0; i < newList.length; i++) {
    console.log(newList[i])
}

for (let i = 0; i < newList1.length; i++) {
    console.log(newList1[i])
}
let numbers = newList1.filter(item => typeof item === "number")
console.log(numbers)
let sum = numbers.reduce((acc, curr) => acc + curr, 0)
console.log(sum)