def gradingStudents(grades):
    # Write your code here
    rounded = []
    for grade in grades:
        rem = grade%5
        if grade > 37 and rem > 2:
            rounded.append(grade + 5 - rem)
        else:
            rounded.append(grade)
            
    return rounded
