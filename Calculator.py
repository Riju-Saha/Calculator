# addition function
def add(ar1):
    res = 0
    for i in range(len(ar1)):
        res += ar1[i]
    return res


# subtraction function
def sub(ar1):
    res = ar1[0]
    for i in list(range(1, len(ar1))):
        res -= ar1[i]
    return res


# multiplication function
def multi(ar1):
    res = 1
    for i in range(len(ar1)):
        res *= ar1[i]
    return res


# division function
def div(ar1):
    res = ar1[0]
    for i in list(range(1, len(ar1))):
        res /= ar1[i]
    return res


# exponential function
def exp(ar1):
    res = ar1[0]
    for i in list(range(1, len(ar1))):
        res **= ar1[i]
    return res


# modulus function
def mod(ar1):
    res = ar1[0]
    for i in list(range(1, len(ar1))):
        res %= ar1[i]
    return res


# hcf function
def hcf(ar1):
    flag = 0
    maximum = (max(ar1)) + 1
    maxi = []
    for i in range(1, maximum):
        for k in range(len(ar1)):
            if ar1[k] % i != 0:
                flag = 0
                break
            else:
                flag = 1
                continue
        if flag == 1:
            maxi.append(i)
    maximum = max(maxi)
    return maximum


# lcm function
def lcm(ar1):
    boolea = False
    prod = 1
    n = 2
    while not boolea:
        abc = 0
        flag = 0
        for k in range(len(ar1)):
            if ar1[k] % n == 0:
                ar1[k] = ar1[k] / n
                abc = 0
            else:
                abc += 1
        # prod *= n
        if abc != len(ar1):
            prod *= n
        if abc == len(ar1):
            n += 1
        else:
            n = 2
        for k in range(len(ar1)):
            if ar1[k] == 1:
                flag += 1
            else:
                flag = 0
        if flag == len(ar1):
            boolea = True
        else:
            boolea = False
    return prod


# user_input to the list
def user_input(ar1):
    user_stop = " "
    while user_stop != "STOP":
        print("Enter your number or write stop to terminate")
        n = input()
        print()
        if n.isdigit():
            n = int(n)
            ar.append(n)
            continue
        else:
            if n.isalpha():
                user_stop = n.upper()
                if user_stop != "STOP":
                    print("Check your input")
                    continue
    return ar1


print("*********************************Simple Calculator*********************************")
print("You will be allowed to enter any number of input of numbers at a time until you write STOP ")
ar = []
user_string, again, user_exp, result = " ", 1, 1, 1

# operation choice
while again == 1:
    print("Press 1 for Addition")
    print("Press 2 for Subtraction")
    print("Press 3 for Multiplication")
    print("Press 4 for Division")
    print("Press 5 for Exponentiation")
    print("Press 6 for Modulus")
    print("Press 7 for Highest Common Factor")
    print("Press 9 for Mixed Expression")
    print("Press 10 to Exit")
    print("Enter your choice -->  ")
    user_choice = int(input())
    # addition
    if user_choice == 1:
        user_input(ar)
        result = add(ar)
        print("Your result is ", result)

    # subtraction
    elif user_choice == 2:
        user_input(ar)
        result = sub(ar)
        print("Your result is ", result)

    # multiplication
    elif user_choice == 3:
        user_input(ar)
        result = multi(ar)
        print("Your result is ", result)

    # division
    elif user_choice == 4:
        user_input(ar)
        result = div(ar)
        print("Your result is ", result)

    # exponentiation
    elif user_choice == 5:
        user_input(ar)
        result = exp(ar)
        print("Your result is ", result)

    # modulus
    elif user_choice == 6:
        user_input(ar)
        result = mod(ar)
        print("Your result is ", result)

    # highest common factor
    elif user_choice == 7:
        user_input(ar)
        result = hcf(ar)
        print("Your result is ", result)

    # least common multiple
    elif user_choice == 8:
        user_input(ar)
        result = lcm(ar)
        print("Your result is ", result)

    # mixed expression
    elif user_choice == 9:
        print(
            "Note: You are allowed to enter only one expression containing more than 2 operands and more than 2 "
            "different operators among those given below only.\n "
            "Type '+' for addition\n"
            "Type '-' for subtraction\n"
            "Type '*' for multiplication\n"
            "Type '/' for division\n"
            "Type '**' for exponent\n"
            "Type '%' for modulus\n")
        print("Enter your mathematical expression, following the rules given above")
        expression = str(input())
        expression = expression.strip()
        for j in range(0, len(expression) + 1, 2):
            if not expression[j].isdigit():
                print("Please check your expression and try again")
                break
        for j in range(1, len(expression), 2):
            # print(j)
            if expression[j] != "+" and expression[j] != "-" and expression[j] != "*" and expression[j] != "/" and \
                    expression[j] != "**" and expression[j] != "%":
                print("Please rectify your operator placements and try again")
                break
        result = eval(expression)
        print("Your result is ", result)
        break

    # exit
    elif user_choice == 10:
        print("Program has terminated successfully")
    else:
        print("Wrong Input")

    print("\n\nPress 1 to rerun the program again.")
    print("Press any number to terminate completely.\n")
    print("Enter your choice.")
    again = int(input())

    # complete termination part
    if again != 1:
        quit()
    # rerun part
    else:
        print("Press 1 to rerun the program from the starting.")
        print("Press any number to rerun the program with the result displayed.")
        print("Enter your choice")
        program_again = int(input())

        if program_again == 1:  # rerun without the result
            again = 1
            continue
        else:  # rerun with the result
            ar.clear()
            ar.append(result)
            again = 1
            continue
