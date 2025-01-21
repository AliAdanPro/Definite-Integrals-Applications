import math
from scipy.integrate import quad
import matplotlib.pyplot as plt
import numpy as np

# 1. Fuel Consumption Calculation
def fuel_consumption_rate(speed, a, b, c):
    return a * speed**2 + b * speed + c

def speed_over_time(time, base_speed, amplitude, frequency):
    return base_speed + amplitude * np.sin(frequency * time)

def fuel_rate_over_time(time, base_speed, amplitude, frequency, a, b, c):
    speed = speed_over_time(time, base_speed, amplitude, frequency)
    return fuel_consumption_rate(speed, a, b, c)

# 2. Consumer Surplus Calculation
def demand_function(price):
    return 100 - 2 * price  # Example demand curve: Q = 100 - 2P

# Graph Functions
def plot_fuel_consumption(base_speed, amplitude, frequency, a, b, c, start_time, end_time):
    times = np.linspace(start_time, end_time, 500)
    speeds = speed_over_time(times, base_speed, amplitude, frequency)
    fuel_rates = fuel_consumption_rate(speeds, a, b, c)

    plt.figure(figsize=(10, 6))
    plt.plot(times, speeds, label="Speed (km/h)", color="blue")
    plt.plot(times, fuel_rates, label="Fuel Rate (L/h)", color="green")
    plt.title("Speed and Fuel Consumption Over Time")
    plt.xlabel("Time (hours)")
    plt.ylabel("Speed (km/h) & Fuel Rate (L/h)")
    plt.legend()
    plt.grid()
    plt.show()

def plot_consumer_surplus(price_market, price_max):
    prices = np.linspace(price_market, price_max, 500)
    quantities = demand_function(prices)

    plt.figure(figsize=(10, 6))
    plt.plot(prices, quantities, label="Demand Curve", color="orange")
    plt.fill_between(prices, quantities, alpha=0.3, label="Consumer Surplus")
    plt.title("Consumer Surplus")
    plt.xlabel("Price")
    plt.ylabel("Quantity Demanded")
    plt.legend()
    plt.grid()
    plt.show()

# Main function to calculate both applications
def main():
    while True:
        print("\nWhat do you want to calculate?")
        print("1. Fuel Consumption")
        print("2. Consumer Surplus")
        print("3. Both")
        print("4. Exit")
        choice = int(input("Enter your choice (1, 2, 3, or 4): "))

        if choice == 1 or choice == 3:
            # Fuel Consumption Inputs
            print("\n=== Fuel Consumption Calculation ===")
            start_time = float(input("Enter start time (hours): "))
            end_time = float(input("Enter end time (hours): "))
            base_speed = float(input("Enter base speed (km/h): "))
            amplitude = float(input("Enter speed variation amplitude: "))
            frequency = float(input("Enter speed variation frequency: "))
            a = float(input("Enter coefficient a for fuel rate: "))
            b = float(input("Enter coefficient b for fuel rate: "))
            c = float(input("Enter coefficient c for fuel rate: "))

            # Calculate total fuel consumption
            total_fuel, _ = quad(
                fuel_rate_over_time, start_time, end_time, 
                args=(base_speed, amplitude, frequency, a, b, c)
            )
            print(f"\nTotal fuel consumed over {end_time - start_time} hours: {total_fuel:.2f} liters")

            # Plot fuel consumption graph
            plot_fuel_consumption(base_speed, amplitude, frequency, a, b, c, start_time, end_time)

        if choice == 2 or choice == 3:
            # Consumer Surplus Inputs
            print("\n=== Consumer Surplus Calculation ===")
            price_market = float(input("Enter market price: "))
            price_max = float(input("Enter maximum price consumers are willing to pay: "))

            # Check if market price exceeds maximum price
            if price_market > price_max:
                print("Consumer Surplus: 0 units (No transaction occurs as market price is higher than what consumers are willing to pay).")
            else:
                # Calculate consumer surplus
                consumer_surplus, _ = quad(demand_function, price_market, price_max)
                
                # Ensure consumer surplus is not negative
                if consumer_surplus < 0:
                    consumer_surplus = 0
                    print("Consumer Surplus is adjusted to 0 units (Negative surplus isn't possible).")
                
                print(f"Consumer Surplus: {consumer_surplus:.2f} units")

                # Plot consumer surplus graph
                plot_consumer_surplus(price_market, price_max)

        if choice == 4:
            print("Exiting program. Goodbye!")
            break

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select 1, 2, 3, or 4.")

# Run the main function
if __name__ == "__main__":
    main()

