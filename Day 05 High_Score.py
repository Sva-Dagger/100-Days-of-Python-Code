# Input a list of student scores
student_scores = input("Enter Students Score : ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
Highest_score = max(student_scores)
print(f"The highest score in the class is: {Highest_score}")
# Write your code below this row 👇
