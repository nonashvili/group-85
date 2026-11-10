let products = [
    { id: 1, name: "Laptop", category: "Electronics", price: 2500, rating: 4.8, inStock: true },
    { id: 2, name: "Phone", category: "Electronics", price: 1800, rating: 4.5, inStock: false },
    { id: 3, name: "Headphones", category: "Accessories", price: 300, rating: 4.2, inStock: true },
    { id: 4, name: "Keyboard", category: "Accessories", price: 450, rating: 3.9, inStock: true },
    { id: 5, name: "Monitor", category: "Electronics", price: 1200, rating: 4.9, inStock: false },
    { id: 6, name: "Mouse", category: "Accessories", price: 150, rating: 4.6, inStock: true },
    { id: 7, name: "Tablet", category: "Electronics", price: 900, rating: 3.7, inStock: true }
]
products.forEach(function(item) {
    console.log(item.name + " costs " + item.price + " GEL")
})
products.forEach(function(item) {
    if (item.inStock) {
        console.log(item.name)
    }
})

let electronics = products.filter(function(item) {
    if (item.category === "Electronics") {
        return item
    }
})

console.log(electronics)

let expensive = products.filter(function(item) {
    if (item.price > 500 && item.rating > 4.5) {
        return item
    }
})

console.log(expensive)

let notAvailable = products.filter(function(item) {
    if (item.inStock === false) {
        return item
    }
})
console.log(notAvailable)

let namesAndPrices = products.map(function(item) {
    return item.name + " - " + item.price + " GEL"
})
console.log(namesAndPrices)

let newPrices = products.map(function(item) {
    return {
        id: item.id,
        name: item.name,
        category: item.category,
        price: item.price + 100,
        rating: item.rating,
        inStock: item.inStock
    }
})

console.log(newPrices)

let monitor = products.findIndex(function(item) {
    return item.name === "Monitor"
})

console.log(monitor)

let rating = products.findIndex(function(item) {
    return item.rating < 4
})

console.log(rating)

let expensiveProduct = products.some(function(item) {
    return item.price > 2000
})

console.log(expensiveProduct)
let unavailableProduct = products.some(function(item) {
    return item.inStock === false
})

console.log(unavailableProduct)
let allPrices = products.every(function(item) {
    return item.price > 100
})

console.log(allPrices)
let allRatings = products.every(function(item) {
    return item.rating > 3.5
})

console.log(allRatings)

let availableProducts = products.filter(function(item) {
    return item.inStock === true
})

let productList = availableProducts.map(function(item) {
    return item.name + " - " + item.price + " GEL"
})
productList.forEach(function(item) {
    console.log(item)
})