from turtle import st


# Program that calculates maximum score using loops

student_scores = input("Input a list of student score ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

max_score = 0
for student_score in student_scores:
    if student_score > max_score:
        max_score = student_score
print("The highest score in the class is: ", max_score)