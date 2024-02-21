#List the odd and even numbers between 0 and 10

numbers1 = []
numbers2 = []
for i in range(10):
    if i % 2 == 0:
        numbers1.append(i)
    
    else:
        numbers2.append(i)


print(f"The odd_numbers between 1 and 10 are {numbers1}")
print(f"The even_numbers between 1 nd 10 are {numbers2}")