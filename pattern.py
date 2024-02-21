#assign the variables star and index gets a place value for the moment as it will be used in two different ways

stars = "*****"
index = ""

# the program prints a different number of stars as it loops through the range.

for i in range(1,10):
   
    if i <= 5:
        index = i
        print(stars[0:index])

    elif i > 5:
        index = 10 - i
        print(stars[0:index]) 

