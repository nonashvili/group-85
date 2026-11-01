let university = {
    name: "Tbilisi University",
    address: {
        city: "Tbilisi",
        building: {
            number: 10,
            floors: 6
        }
    },
    department: {
        name: "Computer Science",
        students: ["marita", "Ana", "levana", "Mariamia"],
        teacher: {
            name: "Luka",
            subjects: ["JavaScript", "Python", "Reacted"]
        }
    },
    library: {
        books: {
            programming: ["JavaScript Basic", "Learn Python"],
            databases: ["SQL Guide", "MongoDB Basics"]
        }
    }
}

console.log(university.address.building.number)
university.address.city = "Qutaisi"
delete university.address.building.floors
console.log(university.department.teacher.subjects[1])
university.department.teacher.subjects.push("C++")
university.department.teacher.name = "sabaaa"
delete university.library.books.programming


for (let i = 0; i < university.library.books.databases.length; i++) {
    if (university.library.books.databases[i].length > 10) {
        console.log(university.library.books.databases[i])
    }
}