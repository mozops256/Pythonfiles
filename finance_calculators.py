import math

print('''Investment - to calculate the amount of interest you will earn on your investment
 bond       -  to calculate the anount you'll have to pay on a home loan
       ''')

answer = input("Enter either investment or bond from the menu above to proceed: ")

# a while loop to check for the wrong input 

while answer.lower() != "investment" and answer.lower() != "bond":
    print("Wrong entry. Please only choose between investment or bond")
    answer = input("Enter either investment or bond from the menu above to proceed: ")


# write an if statement to state the outcomes of selecting either bond or investment

if answer == "investment":
    p = int(input("Please enter the amount of money you are depositing: "))
    r = float(input("Please enter the interest rate: ")) * float(0.01)
    t = int(input("Please enter the number of years you will invest for: "))
    interest = input("Would you prefer either Simple or Compound interest? ")

    while interest.lower() != "simple" and interest.lower() != "compound":
        print("Wrong entry. Please only choose between simple and compound interest.")
        interest = input("Would you prefer either Simple or Compound interest? ")

 
    if interest == "simple":
        A = p *(1 + r*t)
        
        print(f"The total amount after {t} years is {A}")
    
    elif interest == "compound":
        A = p * math.pow((1 + r),t)

        print(f"The total amount after {t} years is {A}")


elif answer == "bond":
    p = int(input("Please enter the value of the house  "))
    i = (float(input("Please enter the annual interest rate  "))* float(0.01))/(12)
    n = int(input("How many months will the loan be repaid?  "))

    repayment = (i*p)/(1-(1 + i)**(-n))

    print(f"You will payback {repayment} per month")        
