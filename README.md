# Applications of Definite Integrals in Real-Life Problems

This project demonstrates how definite integrals can solve real-world problems through **Fuel Consumption Analysis** and **Consumer Surplus Calculation**. Python is used for calculations and visualizations, leveraging libraries like `SciPy`, `Matplotlib`, and `NumPy`.

## Features

1. **Fuel Consumption Analysis**:
   - Calculates total fuel consumed over a given time interval.
   - Plots speed and fuel consumption rate over time.

2. **Consumer Surplus Calculation**:
   - Computes consumer surplus from a demand curve and market price.
   - Plots the demand curve with a shaded surplus region.

## Graphical Outputs

The project generates insightful graphs:
- **Speed vs. Fuel Consumption Rate**
![image](https://github.com/user-attachments/assets/3ba6cdbb-8231-4275-81f1-d1912fc59329)


- **Demand Curve with Consumer Surplus**
![image](https://github.com/user-attachments/assets/5d651ce0-39f6-42b6-b805-83c532e3e377)




## How It Works

### 1. Fuel Consumption Analysis
- **Fuel Rate Function**: Modeled as a quadratic function of speed.
- **Speed Over Time**: Simulated using a sinusoidal function.
- **Integration**: Computes total fuel consumption using definite integrals.

### 2. Consumer Surplus Calculation
- **Demand Curve**: Represents quantity demanded at a given price.
- **Integration**: Calculates the area under the demand curve above the market price.

---
### Inputs Required

#### For Fuel Consumption:
- Start and end time (in hours)
- Base speed (km/h), amplitude, and frequency of speed variation
- Coefficients `a`, `b`, and `c` for the fuel rate function

#### For Consumer Surplus:
- Market price
- Maximum price consumers are willing to pay


## Examples

### Fuel Consumption:
**Input:**  
- Start Time: `0 hours`  
- End Time: `5 hours`  
- Base Speed: `60 km/h`  
- Amplitude: `20 km/h`  
- Frequency: `1 cycle/hour`  
- Coefficients: `a=0.01, b=0.5, c=2`  

**Output:**  
- Total Fuel Consumed: `374.9 liters`  

**Graph:** Speed and fuel consumption rate over time.

### Consumer Surplus:
**Input:**  
- Market Price: `$20`  
- Maximum Price: `$50`  

**Output:**  
- Consumer Surplus: `900 units`  

**Graph:** Demand curve with shaded surplus area.

---

## Applications

1. **Transportation**: Analyze and optimize fuel efficiency using consumption patterns.
2. **Economics**: Understand market dynamics through consumer surplus calculations.

---

## References

- **Python Libraries**:
  - `Matplotlib`: For graph plotting
  - `SciPy`: For numerical integration
  - `NumPy`: For mathematical computations
