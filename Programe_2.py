# Program to check and print if a given temperature is:
# 1.Cold if below 15°C
# 2.Warm if between 15°C and 25°C
# 3.Hot if above 25°

temperature = float(input("Enter the temperature in °C: "))
if temperature < 15:
    print("Cold")
elif 15 <= temperature <= 25:
    print("Warm")
else:
    print("Hot")