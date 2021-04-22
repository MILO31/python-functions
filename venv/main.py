def hotel_cost(nights):
    return 140 * nights


def plane_ride_cost(city):
    if city == "Cape Town":
        return 2500
    elif city == "Durban":
        return 2300
    elif city == "JHB":
        return 2000
    elif city == "BFN":
        return 1800


def rental_car_cost(days):
    if 0 < days <= 2:
        price = 40 * days
    elif 3 >= days <= 6:
        price = (40 * days) - 20
    else:
        price = (40 * days) - 50

    return price


def new_sum(*numbers):
    return sum(numbers)


def trip_cost(city, days, spending_cost):
    return new_sum(hotel_cost(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_cost)


spend = int(input("How much spending money do you have? "))
night = int(input("How long are you staying?"))
plane = input("Where are you travelling to?")
car = int(input("How long will you be renting a car?"))

print("Hotel cost: R", hotel_cost(night))
print("Spending money: R", spend)
print("Plane ride cost: R", plane_ride_cost(plane))
print("Rental car: R", rental_car_cost(car))
print("Trip cost: R", trip_cost(plane, night, spend))
