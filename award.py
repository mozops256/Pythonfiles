#first we define variables and request input for the times each sport will take in minutes

s = int(input("Please enter your swimming time in minutes: "))
c = int(input("Please enter your cycling time in minutes: "))
r = int(input("Please enter your running time in minutes: "))
total = s + c + r

#we can then use the total time to determine which award the contestants will get using logical operatons

if total <= 100:
    print("You have received the Provincial Colours Award")

elif total >= 101 and total <= 105:
    print("You have received the Provincial Half Colours Award")

elif total >=106 and total <= 110:
    print("You have received the Provincial Scroll Award")

else:
    print ("Unfortunately you did not receive an award this time.")
