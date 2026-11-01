let product = {
    productName: "Laptop",
    price: 1500,
    quantity: 3,
    inStock: true,

    allProdPrice: function() {
        return this.price * this.quantity
    },

    isStock: function() {
        return this.inStock
            ? "yes we have thiss product"
            : "no we dont have this productt"
    }
}
console.log(product.allProdPrice())
console.log(product.isStock())