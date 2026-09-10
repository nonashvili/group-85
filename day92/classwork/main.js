let name = ''

let nameForGreeting = name || 'guest'

console.log(`hello ${nameForGreeting} how you doing?` ) 

// რადგან name ცვლადი ცარიელი იყო, console ში გამოვიდა 'guest'