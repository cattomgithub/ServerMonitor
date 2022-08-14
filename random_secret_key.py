import string
import random

LENGTH = 50

result = ''.join(
    random.SystemRandom().choice(string.ascii_letters + string.digits)
    for _ in range(LENGTH)
)

with open("secret_key","x") as file:
    file.write(result)