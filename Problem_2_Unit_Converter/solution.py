print("Which conversion would you like to do?")
print("0. Meters to Centimeters")
print("1. Centimeters to Meters")
choice = input("Enter 0 or 1: ")
if choice == "0":
    meters = float(input("Enter value in meters: "))
    centimeters = meters * 100
    print("Value in centimeters: " + str(centimeters) + "cm")
elif choice == "1":
    centimeters = float(input("Enter value in centimeters: "))
    meters = centimeters / 100
    print("Value in meters: " + str(meters) + "m")
else:
    print("Invalid choice.")
