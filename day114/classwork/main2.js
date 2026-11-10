let player = {
    _name: "Shadow",
    _level: 15,
    _experience: 850,
    _health: 75,
    _isOnline: true,
    get name() {
        if (this._name.length < 3) {
            return "nvalid name!"
        } else {
            return this._name
        }
         },
    get level() {
        if (this._level >= 10) {
            return "advanced Player"
        } else if (this._level >= 5) {
            return "intermediate Player"
        } else {
            return "beginner Player"
        }
    },
    get status() {
        if (this._health === 0) {
            return "player is dead"
        } else if (this._health < 30) {
            return "Critical condition"
        } else {
            return "player is healthy"
        }
    }
}
console.log(player.name)
console.log(player.level)
console.log(player.status)