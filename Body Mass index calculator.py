height=float(input("Enter your height in centimeter: "))
weight=float(input("Enter your height in kg: "))
#dividing by 100 to convert height into meter
height=height/100
#formula for BMI is weight/(height*height)
BMI=weight/(height*height)
print("Your Body Mass Index is: ",BMI)
if (BMI>0):
    if (BMI<15):
        print("You are severely underweighted")
    elif(BMI<18.5):
        print("You are Underweighted ")
    elif(BMI<25):
        print("You are healthy")
    elif(BMI<30):
        print("You are overweighted")
    else:
        print("You are severely overweighted")    
else:
    print("Enter valid inputs")        
        

