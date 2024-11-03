import time,random

name=input("What is your name?")
#It will take a pause of 2 second
time.sleep(2)
print("Hello", name)

feeling=input("How are u feeling today: ")
time.sleep(2)
if "good" in feeling:
    print("I am feeling good too")
else:
    print("Sorry to hear that.")

favcolor=input("Whats your favourite color? ")
time.sleep(2)
color=["Red","Green","Black"]
print("Oh nice!!My favourite color is: "+random.choice(color))