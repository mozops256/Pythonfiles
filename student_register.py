# Request for user input 

no_of_students = int(input("Please enter in figures the number of students registering? "))

# Open the file for writing and insert a for loop to create an ID entry for each registered student

with open('reg_form.txt', 'w') as f:

    for i in range(no_of_students):
        f.write((input("Enter Student ID: ")) + '\n')
        f.write(('.'*10) + '\n')