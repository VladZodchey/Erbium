import string
import random

tokens = open('tokens.txt', 'w', encoding='utf-8')
amount = int(input('Token amount: '))
length = int(input('Token length: '))

for i in range(amount):
    token = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k=length))
    print(token)
    tokens.write(token + '\n')

tokens.close()
