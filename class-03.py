# Decision Structures

age = 16

# Example 01
if age < 18:
    print('Person who needs a legal guardian.')
else:
    print('Legally responsible person.')

vehicle = {'type': 'car', 'brand': 'Fiat', 'power': '140'}

# Example 02
if vehicle['type'] == 'motorcycle':
    print('The vehicle is a motorcycle')
else:
    print('The vehicle is a car')

# Example 03
if vehicle['type'] == 'car' and vehicle['brand'] == 'Fiat':
    print('The vehicle is a car')
else:
    print('The vehicle is a motorcycle')
