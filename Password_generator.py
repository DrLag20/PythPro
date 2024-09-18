import random

Characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
Password_size = int(input("Type in how long your password will be (Type in a number):"))
Password_result = ""

for i in range(Password_size):
    Password_result += random.choice(Characters)

print (Password_result)