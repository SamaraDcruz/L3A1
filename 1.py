print("Welcome to Python Data Types!")

print("Choose the type of your input:")
print("1. Integer")
print("2. Float")
print("3. Text(String)")
print("4. Boolean (True/False)")

choice = input("Enter 1, 2, 3, or 4: ")
user_input = input("Type your value: ")

if choice == "1":
    value = int(user_input)
elif choice == "2":
    value = float(user_input)
elif choice == "4":
    value = user_input == "True"
else:
    value = user_input

print("You entered:", value)
print("Python sees it as:", type(value))

