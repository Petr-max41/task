grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades[0] = (5+3+3+5+4)/5
grades[1] = (2+2+2+3)/4
grades[2] = (4+5+5+2)/4
grades[3] = (4+4+3)/3
grades[4] = (5+5+5+4+5)/5
print(grades)
students = list(students)
print(students)
students[0] = 'Aaron'
students[1] = 'Bilbo'
students[2] = 'Johnny'
students[3] = 'Khendrik'
students[4] = 'Steve'
print(students)
average_score = {students[0]: grades[0],students[1]: grades[1],students[2]: grades[2],students[3]: grades[3],students[4]: grades[4] }
print(average_score)