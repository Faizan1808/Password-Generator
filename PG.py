import random
import string


print('Hello, Welcome to password generator!')

length = int(input('\nEnter the length of password: '))

lower = string.ascii_lowercase

upper = string.ascii_uppercase

num = string.digits
print(num)
symbols = string.punctuation

all = lower +upper + num + symbols
temp = random.sample(all , length)

password = "".join(temp)
print(f'Random Password: {password}')


