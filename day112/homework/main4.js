
let orders = [
    { id: 101, customer: "Nika", total: 250, status: "delivered" },
    { id: 102, customer: "Ana", total: 80, status: "pending" },
    { id: 103, customer: "Gio", total: 420, status: "delivered" },
    { id: 104, customer: "Mariam", total: 150, status: "cancelled" },
    { id: 105, customer: "Luka", total: 310, status: "pending" }
]

orders.forEach(order => {
    console.log(order.id, order.customer)
})
console.log("----------------")
orders.forEach(order => {
    if (order.status === "delivered") {
        console.log(order);
    }
})
console.log("----------------")
orders.forEach(order => {
    if (order.total > 200) {
        console.log(order.id)
    }
})
console.log("----------------")
let pendingCount = 0
orders.forEach(order => {
    if (order.status === "pending") {
        pendingCount++
    }
})

console.log("Pending orders:", pendingCount)

console.log("----------------")

let totalPrice = 0
orders.forEach(order => {
    totalPrice += order.total
})

console.log("Total price:", totalPrice)

console.log("----------------")

let expensiveOrders = []

orders.forEach(order => {
    if (order.total > 200 && order.status === "delivered") {
        expensiveOrders.push(order)
    }
});

console.log(expensiveOrders)
