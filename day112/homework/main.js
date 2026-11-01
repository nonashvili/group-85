let employees = [
    { name: "Giorgi", salary: 2500, department: "IT" },
    { name: "Nino", salary: 1800, department: "HR" },
    { name: "David", salary: 3200, department: "IT" },
    { name: "Maka", salary: 1500, department: "Sales" },
    { name: "Saba", salary: 2800, department: "Sales" }
];
employees.forEach(employee => {
    console.log(employee.name, employee.salary)
});

console.log("----------------")

employees.forEach(employee => {
    if (employee.department === "IT") {
        console.log(employee);
    }
})

console.log("----------------")

employees.forEach(employee => {
    if (employee.salary > 2000) {
        console.log(employee.name)
    }
})

console.log("----------------")

let salesCount = 0

employees.forEach(employee => {
    if (employee.department === "Sales") {
        salesCount++;
    }
});

console.log("Sales employees:", salesCount)

console.log("----------------")
let totalSalary = 0

employees.forEach(employee => {
    totalSalary += employee.salary
});

console.log("Total salary:", totalSalary)
