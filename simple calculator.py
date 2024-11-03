#Simple calculator
def add(S,R):
    #This function is used for adding 2 num
    return S+R
def subtract(S,R):
    #This function is used for subtrction 2 num
    return S-R
def multiply(S,R):
    #This function is used for multiplication 2 num
    return S*R
def division(S,R):
    #This function is used for division 2 num
    return S/R

print("Please select a operation")
print("a.add")
print("b.subtract")
print("c.multiply")    
print("d.division")

choice=input("please enter a choice (a/b/c/d)")
num1=int(input("Enter first number"))
num2= int(input("Enter first number"))       

if choice=="a":
          print(num1, "+",num2, "=",add(num1,num2))         
elif choice=="b":
           print(num1, "-" ,num2 ,"=",subtract(num1,num2))
elif choice=="c": 
          print(num1, "*" ,num2 ,"=",multiply(num1,num2))
elif choice=="d": 
          print(num1, "/" ,num2, "=",division(num1,num2))
else:
          print("Invalid input")    
