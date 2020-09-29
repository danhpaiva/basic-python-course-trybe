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

exit_ = True
counter = 0

while exit_:
    counter += 1
    if counter == 5:
        exit_ = False

print('Counter: ' + str(counter))
