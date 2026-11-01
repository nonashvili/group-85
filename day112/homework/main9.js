let characters = [
    { name: "Shadow", level: 15, health: 85, damage: 70 },
    { name: "Blaze", level: 8, health: 95, damage: 45 },
    { name: "Storm", level: 20, health: 60, damage: 90 },
    { name: "Frost", level: 12, health: 80, damage: 65 },
    { name: "Titan", level: 25, health: 100, damage: 55 },
    { name: "Raven", level: 18, health: 40, damage: 85 }
]

let newCharacters = characters.filter(c => c.level >= 10 && c.damage >= 60)

newCharacters.forEach(c => {
    let healthStatus = c.health >= 70 ? "Healthy" : "Weak"

    let powerStatus = c.damage >= 80 ? "Powerful" : "Normal"

    let warning

    if (c.health < 50) {
        warning = "Warning: Low health!"
    } else {
        warning = "Health is stable"
    }

    console.log(c.name + " - " + healthStatus + " - " + powerStatus + " - " + warning)
})