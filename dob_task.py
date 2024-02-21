# Define the variables to be used.

line1 = []
name = []
name1 = ""
dob = []
dob1 = ""

# read and extract the information from the file to save it to an external variable for easier manipulation.

with open ('DOB.txt', 'r+') as file:
    for line in file:
        line1.append(line.split())

#  create for statements to separate the names and dobs and print them out to separate sections.

for x in line1:
    name.append(x[:2])
    dob.append(x[2:])

for y in name:
    name1 = name1 + (' '.join(y)) + '\n'

for z in dob:
    dob1 = dob1 + (' '.join(z)) + '\n'


print("\033[1mName\033[0m")
print(name1)

print("\033[1mDate of Birth\033[0m")
print(dob1)