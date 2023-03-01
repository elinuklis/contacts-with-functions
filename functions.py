#def sareizinat_ar_divi(x):
    #return 2 * x

#def say_hello_to(salutation, name):
    #print(f"{salutation}, {name}!")

#say_hello_to('Labvakar', 'Elizabete')

#1 define funkciju kas parveidos fahrenheit to celsius

# def f_to_c(fahrenheit):
    # return(fahrenheit - 32) * (5/9)

# user_input = float(input('Enter temperature in fahrenheit: '))
# print(f_to_c(user_input))


def convert_temperature(temperature, unit):
    if unit == 'C':
        fahrenheit = temperature * 9 / 5 + 32
        return fahrenheit
    elif unit == 'F':
        celsius = (temperature - 32) * 5 / 9
        return celsius

print(convert_temperature(90, 'F'))