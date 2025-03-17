import math

# Temperature could be an int or a float
temperature = 0

# These will  be floats
potassium_permeability = 0
sodium_permeability = 0
chloride_permeability = 0

# These will be integers
potassium_outside = 0
potassium_inside = 0

sodium_outside = 0
sodium_inside = 0

chloride_outside = 0
chloride_inside = 0

# These are constants
R = 8.314   # Universal Gas Constant
F = 96485   # Faraday's Constant




# Receives input from user based on
# value chosen
def ghk_values(input_option):
    global R
    global F

    option_tracker = 0

    for i in range(0, 3):
        if input_option == 'temperature':
            temperature = eval(input('Temperature: '))
            i += 1
            input_option = input('What value would you like to input next? ')

        elif input_option == 'permeability':
            potassium_permeability = eval(input('Potassium permeability: '))
            sodium_permeability = eval(input('Sodium permeability: '))
            chloride_permeability = eval(input('Chloride permeability: '))
            i += 1
            input_option = input('What value would you like to input next? ')

        elif input_option == 'ionic concentrations':
            potassium_outside = eval(input('[K+]o: '))
            potassium_inside = eval(input('[K+]i: '))
            sodium_outside = eval(input('[Na+]o: '))
            sodium_inside = eval(input('[Na-]i: '))
            chloride_inside = eval(input('[Cl-]o: '))
            chloride_outside = eval(input('[Cl-]i: '))
            i += 1
            input_option = input('What value would you like to input next? ')


# Prompts inputs for temperature value,
# permeability values, or ion concentration values
ghk_values(input('Would you like to enter temperature,'
      ' permeability, or ionic concentrations?'))

# Asks the user whether they have more values
choice = input('Would you like to enter any other values? ')

# If choice is yes, the input process will repeat
# until 'no' is entered.
if choice == 'yes':
    while choice == 'yes':
        ghk_values(input('Would you like to enter temperature,'
        ' permeability, or ionic concentrations?'))
        choice = input('Would you like to enter any other values? ')
# If choice is 'no', the result is outputted.
elif choice == 'no':
    print()
# Notifies the user their input is invalid.
else:
    print('Not a valid input.')
