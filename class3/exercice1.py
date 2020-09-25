import os
os.system('cls')

userName = 'danhpaiva'
password = '12345'
tentatives = 0

print('\tLogin\n')

userNameVerification = input('Enter your user name: ')
passwordVerification = input('Enter your password: ')

# Condition to have 3 attempts
while (userNameVerification != userName) or (passwordVerification != password):
    tentatives += 1
    if tentatives >= 3:
        break

    print('\n\tUsername and password do not match!')

    userNameVerification = input('\nEnter your user name: ')
    passwordVerification = input('Enter your password: ')

# Check to print success message
if(userNameVerification == userName):
    if(passwordVerification == password):
        print('\n\tLogin successfully!')
