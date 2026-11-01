const packets = [120, 505, -45, 999, 14, 700, 33, 842]
const dangerous = packets.some(packet => packet % 7 === 0 && packet > 500)

if (dangerous) {
    const legitimate = packets.filter(packet =>
        packet > 0 && packet % 3 !== 0 && packet < 1000
    )

    console.log("legit paketebi:", legitimate)
} else {
    console.log("sashishi paketi ver moidzebna!")
}