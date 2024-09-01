students = [
    {"name": "Hermione", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus":"Stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus":"Jack Russel Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus":None}
]

# draco has no patronus! python says to put "None" to say empty or no value

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")