let list = ["zaza", "saba", "giorgi", "luka"]

for(let i = 0; i < list.length; i++) {

    if(list[i].length > 5 && list[i].startsWith("g")) {
        console.log(list[i])
    }

}