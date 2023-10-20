number_grade = int(input("Enter your grade here between 0 - 100."))

#Grading curve based on Week 1 Syllabus and Homework lecture video

if number_grade >= 90 and number_grade <= 100:
    letter_grade = "A"

elif number_grade >= 80 and number_grade < 90:
    letter_grade = "B"
    if number_grade >= 87 and number_grade < 90:
        letter_grade = "B+"

elif number_grade >= 70 and number_grade < 80:
    letter_grade = "C"
    if number_grade >= 77 and number_grade < 80:
        letter_grade = "C+"

elif number_grade >= 60 and number_grade < 70:
    letter_grade = "D"
    if number_grade >= 67 and number_grade < 70:
        letter_grade = "D+"

elif number_grade < 60 and number_grade >= 0:
    letter_grade = "F"

else:
    letter_grade = "Please input a number between 0 - 100."

print(letter_grade)