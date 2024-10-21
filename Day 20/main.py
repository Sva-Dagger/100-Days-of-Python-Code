with open("High_score.txt") as File:
    contents = File.read()
    print(contents)

with open("New_score.txt", mode="a") as File:
    contents = File.write("\nNew_file.")
    print(contents)