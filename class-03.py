# Decision Structures

age = 16

# Example 01
if age < 18:
    print('Person who needs a legal guardian.')
else:
    print('Legally responsible person.')

vehicle = {'type': 'car', 'brand': 'Fiat', 'power': 140}

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

# Example 04
result = vehicle['type'] == 'motorcycle'
print(result)
result = vehicle['type'] == 'car'
print(result)

# Example 05
if (vehicle['type'] == 'bus' or vehicle['brand'] == 'Honda') or vehicle['power'] >= 120:
    print('You have a fast vehicle.')
else:
    print('Your vehicle is not fast.')

# Example 06
if vehicle['type'] == 'car':
    print('Car')
elif vehicle['type'] == 'bus':
    print('Bus')
else:
    print('...')

# Example 07

name = 'Daniel Paiva'
if name:
    print('True')
else:
    print('False')

name = ''
if name:
    print('True')
else:
    print('False')

number = 0
if number:
    print('True')
else:
    print('False')

oneList = []
if oneList:
    print('True')
else:
    print('False')

status = None
if status:
    print('True')
else:
    print('False')