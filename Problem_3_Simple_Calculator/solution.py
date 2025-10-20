a = int(input("enter the first number: "))
b = int(input("enter the second number: "))
print("1. addition ")
print("2. subtraction ")
print("3. multiplication ")
print("4. divission ")
choice =input("enter 1 or 2 or 3 or 4 : ")
if choice == "1":
    result = a + b
    print("the sum of this two numbers is " + str(result))
elif choice == "2":
    result = a - b
    print("the result  is " + str(result))
elif choice == "3":
    result = a * b
    print("the multiplication of this two numbers is " + str(result))
elif choice == "4":
    if b != 0:
        result = a / b
        print("the result  is " + str(result))
    else:
        print("it is undefined")
else:
    print("invalid choice")
