student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# Extracting scores into a list
scores_list = list(student_scores.values())
print(scores_list)
names = list(student_scores.keys())
print(names)

student_grades = {}

for i in range(len(scores_list)):
    score = scores_list[i]
    name = names[i]

    if score >= 91 and score <= 100:
        grades = "Outstanding"
    elif score >= 81 and score <= 90:
        grades = "Exceeds Expectations"
    elif score >= 71 and score <= 80:
        grades = "Acceptable"
    elif score <= 70:
        grades = "Fail"
    else:
        grades = "Invalid score"
    student_grades[name] = grades

print(student_grades)


