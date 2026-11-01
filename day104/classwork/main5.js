let scores = [45, 78, 32, 90, 56, 84, 67]

let newScores = scores.map(score => {
    if (score < 60) {
        return score + 10
    } else {
        return score + 5
    }
})
console.log(newScores)
