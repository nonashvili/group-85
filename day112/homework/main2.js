let books = [
    { title: "Harry Potter", price: 35, pages: 320 },
    { title: "The Hobbit", price: 28, pages: 280 },
    { title: "Atomic Habits", price: 45, pages: 250 },
    { title: "The Alchemist", price: 20, pages: 190 },
    { title: "Clean Code", price: 55, pages: 450 }
];

books.forEach(book => {
    console.log(book.title)
})

console.log("----------------")

books.forEach(book => {
    if (book.price < 30) {
        console.log(book.title)
    }
})

console.log("----------------")

books.forEach(book => {
    if (book.pages > 300) {
        console.log(book.title)
    }
})

console.log("----------------")

let expensiveBooks = 0

books.forEach(book => {
    if (book.price > 40) {
        expensiveBooks++;
    }
})

console.log("Expensive books:", expensiveBooks)

console.log("----------------")
let totalPrice = 0

books.forEach(book => {
    totalPrice += book.price
})

console.log("Total price:", totalPrice)

console.log("----------------")

let longBooks = []

books.forEach(book => {
    if (book.pages > 300) {
        longBooks.push(book)
    }
})

console.log(longBooks)
