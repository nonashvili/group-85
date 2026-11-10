let user = {
    _name: "Shadow",
    _email: "shadow@gmail.com",
    _password: "314522",
    get email() {
        return this._email
    },

    set email(newEmail) {
        this._email = newEmail
    },

    get password() {
        return this._password;
    },

    set password(newPassword) {
        this._password = newPassword
    }
}
user.email = "axaliiiishadow@gmail.com"
user.password = "571102259"
console.log(user.email)
console.log(user.password)