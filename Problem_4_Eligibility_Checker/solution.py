age = int(input("Enter your age: "))
license_status = input("Do you have a driver's license? (yes/no): ").lower()

if age >= 18:
    if license_status == "yes":
        print("You are eligible to drive.")
    else:
        print("You are old enough, but you need a driver's license to drive.")
else:
    print("You are not old enough to drive.")
