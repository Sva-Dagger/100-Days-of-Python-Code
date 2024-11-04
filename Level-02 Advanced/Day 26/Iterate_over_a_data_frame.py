import pandas
student_dict = {
    "Student" : ["Angela", "James", "Lily"],
    "score" : [56, 76, 98]
}
student_data_frame = pandas.DataFrame(student_dict)
student_data_frame.to_csv("New_CSV.csv")
print(student_data_frame)
for (index, row) in student_data_frame.iterrows():
    if row.Student == "Angela":
        print(f"{row.Student} score is {row.score}")
