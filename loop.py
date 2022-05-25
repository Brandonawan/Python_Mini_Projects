# Program calculates the average from a list of numbers
# The list can be input define or gotten from user input as the case below

student_heights = input("Input a list of student heights" + "").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

# Here, the number of heights is gotten
height_count = 0
for height in student_heights:
    height_count += 1
print("Total Number = ", height_count)


numbers_of_students = 0
for number in student_heights:
    numbers_of_students += number
print("Total Number of Students ", numbers_of_students)

average = round(numbers_of_students/height_count)
print(average)

