let colors = ["red", "blue", "green", "yellow", "black", "white"]

colors[2] = "purple"
colors[4] = "pink"

let first = colors[0]
colors.splice(0, 1)
colors.push(first)

console.log(colors)
