import secrets
import string

length = int(input('Enter password length: '))
characters = string.ascii_letters + string.digits
password = ''.join(secrets.choice(characters) for i in range(length))
print(password)
