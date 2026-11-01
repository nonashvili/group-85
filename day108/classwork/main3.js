const rawEnergies = [5, 45, 120, 200, 12, 88, -10, 150]
const filteredEnergies = rawEnergies.filter(energy =>
    energy > 10 && energy < 150
)
const quantumCoefficients = filteredEnergies.map(energy =>
    "Q-" + (energy * 3 - 5).toString()
)
console.log(quantumCoefficients)