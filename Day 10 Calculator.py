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