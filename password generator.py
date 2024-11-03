import random

def generatepassword(n):
    characters="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password=""

    for i in range(n):
        password+=random.choice(characters)
    return password

if __name__=="__main__":
    n=12
    password=generatepassword(n)
    print("A random password is generated:",password)        

    

