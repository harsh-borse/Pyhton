name = input("Enter your name: ")
age = int(input("Enter your age: "))
print("Hello!", name, "How are you ?")
print("You are", age, "years old.")
if age < 18:
    print("Since your age is less than 18, \nYou are not eligible to vote.")
else:
    print("You are eligible to vote.")
    