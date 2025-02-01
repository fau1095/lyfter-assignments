
number_one = int(input("Enter the first number: "))
number_two = int(input("Enter the second number: "))
number_three = int(input("Enter the third number: "))

#print the highest number that the user entered, not only the first one
if number_one > number_two and number_one > number_three:
    print(f"The highest number is: {number_one}")
elif number_two > number_one and number_two > number_three:
    print(f"The highest number is: {number_two}")
else:
    print(f"The highest number is: {number_three}")