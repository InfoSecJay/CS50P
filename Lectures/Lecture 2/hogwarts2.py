#bad way to do compare lists
# students = ["Hermione", "Harry", "Ron", "Draco"]
# hourse = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]


# key and value in dictionary
students = {
    "Hermione":"Gryffindor",
    "Harry":"Gryffindor",
    "Ron":"Gryffindor",
    "Draco":"Slytherin"
}


# print(students["Hermione"])


for student in students:
    print(student, students[student], sep=", ")