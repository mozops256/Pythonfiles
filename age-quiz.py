#start
#age => 40 
#age => 101
#age => 65
#age < 13
#age == 21
#else 

age = int(input("Please enter your age: "))

if age < 13:
    print("You qualify for the kiddie discount.")
elif age == 21:
    print("Congrats on your 21st!")
elif age >= 40 and age < 65:
    print("You're over the hill.")
elif age >= 65 and age <= 100:
    print("Enjoy your retirement!")
elif age > 100:
    print("Sorry, you're dead.")
else:
    print("Age is but a number.")