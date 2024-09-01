students = ["Hermione", "Harry", "Ron"]



# print(students[0])

# for student in students:  # didnt call varialbe _ since we are using it 
#     print(student)


"""
the for loop creates a variable for you
assigns the variable to first thing in list, then 2nd thing, then third thing...
and does all the code below

when we do a range, its better
"""
for i in range(len(students)):
    print(i+1, students[i])
    
