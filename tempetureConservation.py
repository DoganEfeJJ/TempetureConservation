unit = input("Is this temperature in Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9*temp) / 5 + 32,1)
    print(temp)
elif unit == "F":
    temp = round((temp - 32) * 9/5,1)
    print(temp)