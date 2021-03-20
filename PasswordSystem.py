
password = ''
storedPassword = 'vikings'
allowedTries = 3
attempts = 0



while password != storedPassword:
    password = input('Enter password: ')
    attempts += 1
    if attempts == allowedTries and password != storedPassword:
        print('Too many tries. Reload page.')
        break
    elif attempts <= allowedTries and password == storedPassword:
        continue
    else:
        print('You have used', attempts, 'attempt(s).')
else:
    print('Access granted.')
