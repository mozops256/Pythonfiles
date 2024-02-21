#create a list called menu with items sold
menu = ['steak', 'chips', 'chicken','lamb']

#create a dictionary called stock with stock value of items from menu list above
stock = {'steak': 10, 'chips': 20, 'chicken': 30, 'lamb': 25}

#create a dictionary called price with items from menu list above
price = {'steak': 30, 'chips': 5, 'chicken': 20, 'lamb': 15}

#total_stock worth is the total amount of stock for each item multiplied by its respective price

#a for loop to calculate stock price

total_stock = 0
for i in menu:
    total_stock += (stock[i] * price[i])


print(f"The total stock worth in the Cafe is: {total_stock}")
