even_num = 0
target = int(input("Enter your target numer : "))
for number in range(1, target+1):
  if number % 2 == 0:
    even_num += number

print(even_num)