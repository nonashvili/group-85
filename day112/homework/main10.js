let athletes = [
    { name: "Nika", sport: "Swimming", age: 21, medals: 5, score: 92 },
    { name: "Mariam", sport: "Tennis", age: 19, medals: 3, score: 85 },
    { name: "Giorgi", sport: "Swimming", age: 24, medals: 7, score: 88 },
    { name: "Ana", sport: "Running", age: 17, medals: 2, score: 95 },
    { name: "Luka", sport: "Tennis", age: 22, medals: 6, score: 78 },
    { name: "Elene", sport: "Swimming", age: 20, medals: 4, score: 96 },
    { name: "Saba", sport: "Running", age: 25, medals: 8, score: 82 },
    { name: "Data", sport: "Tennis", age: 23, medals: 5, score: 91 }
]

let newAthletes = athletes.filter(a => a.sport === "Swimming" && a.medals >= 4)

let totalScore = 0

newAthletes.forEach(a => {

    let result = a.score >= 90 ? "Excellent" : a.score >= 80 ? "Good" : "Needs improvement"

    let medalStatus

    if (a.medals >= 5) {
        medalStatus = "Has 5 or more medals"
    } else {
        medalStatus = "Has less than 5 medals"
    }

    console.log(a.name + " - Age: " + a.age + " - Medals: " + a.medals + " - Score: " + a.score + " - " + result + " - " + medalStatus)

    totalScore += a.score
})

console.log("Total athletes: " + newAthletes.length)
console.log("Total score: " + totalScore)