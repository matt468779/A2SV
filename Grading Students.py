def gradingStudents(grades):
    # Write your code here
    newGrades = []
    for grade in grades:
        if grade >= 38 and grade % 5 >= 3:
            newGrades.append(grade + 5 - ( grade % 5))
        else:
            newGrades.append(grade)

    return newGrades
