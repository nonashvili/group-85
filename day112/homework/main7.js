let students = [
    { name: "Nika", score: 95, attendance: 92 },
    { name: "Mariam", score: 65, attendance: 85 },
    { name: "Giorgi", score: 82, attendance: 70 },
    { name: "Ana", score: 45, attendance: 95 },
    { name: "Luka", score: 90, attendance: 88 },
    { name: "Elene", score: 75, attendance: 96 }
]

let newStudents = students.filter(s => s.score >= 70)

newStudents.forEach(s => {
    let result = s.score >= 90 ? "Excellent" : "Passed"

    let attendanceStatus = s.attendance >= 90 ? "Good attendance" : "Low attendance"

    console.log(s.name + " - Score: " + s.score + " - " + result + " - " + attendanceStatus);
})