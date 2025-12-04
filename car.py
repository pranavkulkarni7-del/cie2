import sys

if len(sys.argv) != 4:
    print("Usage: python program.py <car_type> <fuel_in_liters> <mileage>")
    sys.exit()

car_type = sys.argv[1]
fuel = float(sys.argv[2])
mileage = float(sys.argv[3])

if fuel <= 0:
    print("Fuel must be greater than 0.")
elif mileage <= 0:
    print("Mileage must be greater than 0.")
else:
    total_range = fuel * mileage
    print("Car Type:", car_type)
    print("Fuel:", fuel, "liters")
    print("Mileage:", mileage, "km/l")
    print("Total Travel Range:", total_range, "km")
