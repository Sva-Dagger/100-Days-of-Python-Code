import random

names = ["Siva", "Suresh","Mathi", "Divya", "Raju", "Devi", "Mini"]
students_score = {student:random.randint(1, 100) for student in names}
print(students_score)
High_score = {student:score for (student,score) in (students_score).items() if score >= 60}
print(High_score)