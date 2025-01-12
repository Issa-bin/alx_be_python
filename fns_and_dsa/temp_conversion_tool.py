FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    fahrenheit_to_celsius = ()* FAHRENHEIT_TO_CELSIUS_FACTOR
    print(f"{fahrenheit}°F is {fahrenheit_to_celsius}°C")

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    celsius_to_fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    print(f"{celsius}°C is {celsius_to_fahrenheit}°F")

temperature = input("Enter the temperature to convert: ")
fahrenheit_or_celsius = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").upper()
if temperature.isdigit() and fahrenheit_or_celsius == "F":
        convert_to_celsius(fahrenheit=float(temperature))
elif temperature.isdigit() and fahrenheit_or_celsius == "C":
        convert_to_fahrenheit(celsius=float(temperature))
else:
        print("Invalid temperature. Please enter a numeric value.")