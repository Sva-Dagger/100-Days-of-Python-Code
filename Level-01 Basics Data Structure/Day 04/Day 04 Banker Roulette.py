names_string = "karthi, siva, mano, furi, steven"

names = names_string.split(", ")

import random
num_items = len(names)

random_choice = random.randint(0, num_items - 1)
who_pays_the_bill = names[random_choice]
print(who_pays_the_bill + " is going to buy the meal today!")
