def add(n1,n2):
    """Adds two numbers together"""
    return n1 + n2

def subtract(n1,n2):
    """Adds subtracts n1 from n2"""
    return n1 - n2

def multiply(n1,n2):
    """Multiplies two numbers together"""
    return n1 * n2

def divide(n1,n2):
    """Divides n1 by n2"""
    return n1 / n2

operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


running = True
n1 = int(input("What is the first number?"))
while running == True:
    functions = input("Pick a function: \n+\n-\n*\n/\n")
    n2 = int(input("What is the next number?"))
    funct = operators[functions]


    if funct == add:
        output = add(n1,n2)

    elif funct == subtract:
        output = subtract(n1,n2)

    elif funct == multiply:
        output = multiply(n1,n2)

    else:
        output = divide(n1,n2)

    print(f"{n1} {functions} {n2} = {output}")

    keep_going = input("Do you want to calculate anything else? y/n")

    if keep_going == "y":
        running = True
        n1 = output
    else:
        running = False
