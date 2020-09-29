# Repetition Structure

for i in range(10):
    print(i)

guests = ['Maria', 'Jose', 'Arthur']

for guest in guests:
    print(guest + ' You are invited')

print()

for i in range(len(guests)):
    guest = guests[i]
    print(guest + ' You are invited')

print()

counter = 0

while counter < 5:
    counter += 1

print('Counter: ' + str(counter))
