#We define variables for the user input and a list to store the entered numbers

number = int(input("Please enter a number: "))

numbers = []

while number != -1:
    numbers.append(number)
    number = int(input("Please enter a number: "))

# after the while loop runs, the program prints the list of numbers and calculates their average.

print("")

print(f"The numbers you entered are {numbers}")

average = (sum(numbers)/len(numbers))

print("")

print(f"Their average is {average}")

