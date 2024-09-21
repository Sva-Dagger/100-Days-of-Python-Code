student_heights = input(" Enter Students Height : ").split()
total_height = 0
print(student_heights)
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
for num in student_heights:
  total_height += num
number_of_students = len(student_heights)
average_height = round(total_height/number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {average_height}")
