# Here we will Generate temp data for 365 days and find the hottest and coldest
# day and find the temperature deviation from average and identify outliers very
# High/Low temps.

# Generate temp data for 365 days

import numpy as np

# Here the lowest temp is 8 and highest is 48

temp = np.random.randint(8, 48, size=365)

print("Temperature data for 365 days generated.")
print(temp)

# Find the hottest and coldest day

hottest_day = np.max(temp)
print(f"Hottest day temperature: {hottest_day}°C")

coldest_day = np.min(temp)
print(f"Coldest day temperature: {coldest_day}°C")

# Find average temperature
average_temp = np.mean(temp)
print(f"Average temperature: {round(average_temp, 2)}°C")

# Find temperature deviation from average
deviation = temp - average_temp
print("Temperature deviation from average for each day:")
print(np.round(deviation, 2))

# Identify outliers (very high/low temps) for very high(temp is > 40 and very low < 10)
highest_outliers = temp[temp > 40]
print("Outliers very high temperatures:")
print(highest_outliers)

lowest_outliers = temp[temp < 10]
print("Outliers very low temperatures:")
print(lowest_outliers)

print("Temperature analysis completed.")

print("\n------ End of Project1/project1.py ------")
print("\n")

print("\n------ Analysis Report for temperature data ------\n")

print("1. Temperature data for 365 days has been generated using random integers between 8°C and 48°C.")
print(f"2. The hottest day recorded a temperature of {hottest_day}°C.")
print(f"3. The coldest day recorded a temperature of {coldest_day}°C.")
print(f"4. The average temperature over the year is approximately {round(average_temp, 2)}°C.")
print(f"5. The number of extreme hot days (above 40°C): {len(highest_outliers)}")
print(f"6. The number of extreme cold days (below 10°C): {len(lowest_outliers)}")

print("\n------ End of Analysis Report ------\n")