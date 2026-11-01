let products = [
    { name: "Laptop", price: 2500, rating: 4.8 },
    { name: "Mouse", price: 80, rating: 3.5 },
    { name: "Keyboard", price: 180, rating: 4.6 },
    { name: "Monitor", price: 900, rating: 4.2 },
    { name: "Headphones", price: 350, rating: 4.9 },
    { name: "Tablet", price: 1200, rating: 3.8 }
];

let newProducts = products.filter(p => p.price > 100)

newProducts.forEach(p => {
    let result = p.rating >= 4.5 ? "Excellent" : "Good"

    console.log(p.name + " costs " + p.price + " GEL, Rating: " + result)
})