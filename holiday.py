# A programme to calculate the total cost of a holiday
# A dictionary to represent the different countries/cities

d = {'a': 'Canada', 'b' : 'Brussels', 'c' : 'Kampala'}
city_flight = ""

#The while loop checks the user's input matches one of the keys in the dictionary
while True:        
    print("A selection of Cities and their flight costs\n\ta) Canada - 100 \n","\tb) Brussels - 250\n","\tc) Kampala - 400\n")

    x = input("Please choose a, b or c from the options above: ")

    if x in d:
        city_flight += d[x]
        print(d[x])
        break

    else:
        print("Please try again")


num_nights = int(input("How many nights will you be staying? "))

rental_days = int(input("How many days will you be hiring the car? "))

def hotel_cost(num_nights):
    result = num_nights * 50
    return(result)

def plane_cost(city_flight):
    if city_flight == d['a']:
        return 100

    elif city_flight == d['b']:
        return 250
    elif city_flight == d['c']:
        return 400
        

def car_rental(rental_days):
    result = 70 * rental_days
    return result


def holiday_cost(hotel_cost, plane_cost, car_rental):
    result = hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)
    return result

print(f"\nThe flight cost is {plane_cost(city_flight)}")
print(f"The Car Rental cost is {car_rental(rental_days)}")
print(f"The Hotel cost is {hotel_cost(num_nights)}")
print(f"\nThe total cost of your holiday all inclusive is {holiday_cost(hotel_cost, plane_cost, car_rental)}")