def Add(num1, num2):
    answer = num1 + num2
    print(answer)
    return answer

def Sub(num1, num2):
    answer = num1 - num2
    print(answer)
    return answer

def Mult(num1, num2):
    answer = num1 * num2
    print(answer)
    return answer

def Divide(num1, num2):
    answer = num1 / num2
    print(answer)
    return answer

operations =  {
    "+" : Add,
    "-" : Sub,
    "*" : Mult,
    "/" : Divide
}

num1 = float(input("Enter your 1st number : "))
num2 = float(input("Enter your 2nd number : "))

for symbols in operations:
    print(symbols)
operation_symbol = input("Pick an operation from the line above : ")
caculate_functions = operations[operation_symbol]
answer = float(caculate_functions(num1, num2))
print(f"{num1} {operation_symbol} {num2} = {answer}")
Continue = input("You want to continue the game play Y/N : ")
num1 = answer
num2 = float(input("Enter the new number 2 : "))

if Continue == "Y":
    for symbols in operations:
        print(symbols)
    operation_symbol = input("Pick an operation from the line above : ")
    caculate_functions = operations[operation_symbol]
    answer = float(caculate_functions(num1, num2))
    print(f"{num1} {operation_symbol} {num2} = {answer}")
else :
    print("Thank you for using this")
