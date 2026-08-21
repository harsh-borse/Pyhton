#Write a program to accept marks of 3 Subjects out of 100.
#Calculate total marks and percentage and Calculate Grade as following
#if percentage is >=90, grade is "Distinction"
#if percentage is >=80, grade is "First Class"
#if percentage is >=60, grade is "Second Class"
#if percentage is <35, grade is "Fail"

marks1 = int(input("Enter marks for subject 1: "))
marks2 = int(input("Enter marks for subject 2: "))
marks3 = int(input("Enter marks for subject 3: "))

total_marks = marks1 + marks2 + marks3
percentage = (total_marks / 3)

if marks1 >=40 and marks2 >=40 and marks3 >=40:
    if percentage >= 90:
        grade = "Distinction"
    elif percentage >= 80:
        grade = "First Class"
    elif percentage >= 60:
        grade = "Second Class"
else:
    grade = "Fail"


print("Total Marks:", total_marks)
print("Percentage:", percentage)
print("Grade:", grade)