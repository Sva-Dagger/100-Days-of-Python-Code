def calculate_paint_area(height, width, coverage):
    area_to_paint = height * width
    number_of_cans = area_to_paint / coverage
    if number_of_cans % 1 != 0:
        number_of_cans = int(number_of_cans) + 1
    else:
        number_of_cans = int(number_of_cans)
    return number_of_cans


# Get user input for height and width
test_h = int(input("Enter your wall height : "))
test_w = int(input("Enter your wall width : "))
cover = 5

# Calculate the number of cans needed
number_of_cans = calculate_paint_area(height=test_h, width=test_w, coverage=cover)

print(f"You'll need {number_of_cans} cans of paint.")


