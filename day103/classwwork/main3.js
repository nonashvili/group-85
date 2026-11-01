let player1 = Math.floor(Math.random() * 21) + 10
let player2 = Math.floor(Math.random() * 21) + 10



console.log("Player 1 dzala:", player1)
console.log("Player 2 dzala:", player2)


if (player1 === 20) {
    player1 += 5
}

if (player2 === 20) {
    player2 += 5
}

console.log("Player 1 saboloo dzala:", player1)
console.log("Player 2 saboloo dzala:", player2)  

if (player1 > player2) {
    console.log("Player 1 gaimarjvaaa")
} else if (player2 > player1) {
    console.log("Player 2 gaimarjvaa")
} else {
    console.log("freaa")
}
