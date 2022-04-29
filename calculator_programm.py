# calculator

#add
def add(n1, n2):
    return n1 + n2

#Substract
def substract(n1, n2):
    return n1 - n2
#multiply
def multiply(n1, n2):
    return n1 * n2
#divide
def divide(n1, n2):
    return n1 / n2
#  словарь с переменные -  функции
operations = {
    "+": add,
    "-": substract,
    "*": multiply,
    "/": divide
}

# function = operations["*"]      # из словаря выбираем ключ, которому соответствует функция
# function(2, 3)

def calculator():
    num1 = float(input("What's the first number?: "))
    for key in operations:
        print(key)
    type = 'y'
    while type:
        operation_sumbol = input('pick an operation: ')
        num = float(input("What's the next number?: "))
        function = operations[operation_sumbol]      # из словаря выбираем ключ, которому соответствует функция
        answer = function(num1, num)

        print(f"{num1} {operation_sumbol} {num} = {answer}")

        type = input(f"Type 'y' to continue with {answer} or type 'n' to exit or 'c' to new calculator : ")
        if type == "y":
            num1 = answer
        elif type == "n":
            break
        else:
            type = False
            calculator()

calculator()
