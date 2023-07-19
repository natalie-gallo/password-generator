import random
import string

letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

pwd_length = random.randint(8,16)

password = ''

for i in range(pwd_length):
  password += ''.join(random.choice(alphabet))

print(password)