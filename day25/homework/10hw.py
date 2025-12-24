#შექმენი list: tasks = ["homework", "clean room", "exercise"] მომხმარებელს ჰკითხე Are you sure you want to delete all tasks? (yes/no). თუ "yes" მთლიანად გაასუფთავე ლისთი, თუ "no" არაფერი შეცვალო.

tasks = ["homework", "clean room", "exercise"]

user=input("hello if you type yes the list will be deleted yes or no:")

if user == "yes":
    tasks.clear()

print(tasks)