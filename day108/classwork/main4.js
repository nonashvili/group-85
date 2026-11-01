const tokens_serv1 = ["SEC-0091", "SEC-7821", "SEC-1111", "SEC-999"]
const tokens_serv2 = ["SEC-0091", "SEc-1111", "SEC-1111", "SEC-9999"]
const tokens_serv3 = ["SEC-0000091", "SEC-7821", "SEC-1111"]
const result1 = tokens_serv1.every(token =>
    token.startsWith("SEC-") && token.length >= 8
)
const result2 = tokens_serv2.every(token =>
    token.startsWith("SEC-") && token.length >= 8
)
const result3 = tokens_serv3.every(token =>
    token.startsWith("SEC-") && token.length >= 8
)
console.log("Server 1:", result1)
console.log("Server 2:", result2)
console.log("Server 3:", result3)