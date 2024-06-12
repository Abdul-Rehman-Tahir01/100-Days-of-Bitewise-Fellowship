temperature = input("Enter temperature: \n")
splitted = temperature.split()

magnitude = splitted[0]
unit = splitted[-1]

if(unit.lower()=="celsius"):
    fahrenheit = (int(magnitude)*(9/5)) + 32
    kelvin = int(magnitude) + 273.15
    print(temperature + " is equal to " + str(fahrenheit) + " degree fahrenheit and " + str(kelvin) + " degree kelvin")
elif(unit.lower()=="fahrenheit"):
    celcius = (int(magnitude)-32)*(5/9)
    kelvin = celcius + 273.15
    print(temperature + " is equal to " + str(celcius) + " degree celsius and " + str(kelvin) + " degree kelvin")
elif(unit.lower()=="kelvin"):
    celcius = int(magnitude) - 273.15
    fahrenheit = (celcius*(9/5)) + 32
    print(temperature + " is equal to " + str(fahrenheit) + " degree fahrenheit and " + str(celcius) + " degree celsius")