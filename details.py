#Start
#request string input for the first and last name of the user
#request integer input for the user's age
#request integer input for the users house number
# request string input for the user's streetname
#print using the f-format so the output updates everytime a new input is entered

#using the input() command to get some information from the user

first_name = input("Please enter your first name: ")
last_name = input("Please enter your last name: ")
age = int(input("Please enter your age:"))
house_number = int(input("Please enter your House number: "))
street_name = input("Please enter your street name: ")

#used the f-format with the print command to display the entered information
print(f"This is {first_name} {last_name}. He is {age} years old and lives at house number {house_number} on {street_name}.")