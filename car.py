import sys


def main():
    if len(sys.argv) != 4:
        print("Usage: python car.py <car_type> <fuel_in_litre> <mileage>")
        sys.exit(1)

    car_type = sys.argv[1]
    try:
        fuel = float(sys.argv[2])
        mileage = float(sys.argv[3])
    except ValueError:
        print("Fuel and mileage must be numeric values.")
        sys.exit(1)

    if fuel <= 0:
        print("Fuel in litre should be greater than 0")
        sys.exit(1)
    elif mileage <= 0:
        print("Mileage should be greater than 0")
        sys.exit(1)

    total_range = fuel * mileage
    print(f"Car Type: {car_type}, Fuel: {fuel} litre, Mileage: {mileage} km/l")
    print(f"The total range of the {car_type} is {total_range} km.")


