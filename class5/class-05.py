age = 27

print('My age is: ' + str(age))

print('My age is: {}'.format(age))

print(f'My age is: {age}')  # More efficient

name = 'Daniel Paiva'

print(f'My name is {name} and I am {age} years old')

name = 'Daniel Paiva qnoqicnqicnqcinspncipcnpqcnqpcnqpcq'

print(f'My name is {name:.12} and I am {age:05} years old')

money = 2.5

print(f'I have {money:.2f} R$')

list_itens = ['Fork', 'Knife', 'Glass', 'Plate']

print(f'I lunch with {list_itens[0]} and {list_itens[1]} in {list_itens[-1]}')

print(f'I will be {age + 30} years old in 30 years')
