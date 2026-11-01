
let players = [
    { name: "Sandro", sport: "Football", goals: 12 },
    { name: "Elene", sport: "Tennis", goals: 8 },
    { name: "Lasha", sport: "Football", goals: 19 },
    { name: "Tako", sport: "Basketball", goals: 15 },
    { name: "Data", sport: "Football", goals: 6 }
]

players.forEach(player => {
    console.log(player.name, player.sport)
});

console.log("----------------")
players.forEach(player => {
    if (player.sport === "Football") {
        console.log(player.name);
    }
});

console.log("----------------")
players.forEach(player => {
    if (player.goals > 10) {
        console.log(player.name)
    }
})

console.log("----------------")
let footballCount = 0

players.forEach(player => {
    if (player.sport === "Football") {
        footballCount++
    }
})

console.log("Football players:", footballCount)

console.log("----------------")
let totalGoals = 0

players.forEach(player => {
    totalGoals += player.goals
});

console.log("Total goals:", totalGoals)

console.log("----------------")
let topPlayers = []

players.forEach(player => {
    if (player.goals >= 10) {
        topPlayers.push(player)
    }
})

console.log(topPlayers)
