import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

while 1:
    length = int(input("length of password "))
    count = int(input("count of password : "))

    for x in range(0, count):
        password = ""
        for x in range(0, length):
            password_char = random.choice(chars)
            password = password + password_char
        print(f"passwords: {password}")
