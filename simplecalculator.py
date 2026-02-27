def add(a,b) :
  return a + b
def subtract(a,b) :
  retrun a - b 
def multiply(a,b) :
  return a * b 
def division(a,b) :
  return a/b

print(--**SIMPLE CALCULATOR**--)
print("1.ADDITION")
print("2.SUBTRACTION")
print("3.MULTIPLICATION")
print("4.DIVISON")

choice = int(input("Choose any option : ")

a = float(input("Enter any number : ")
b = float(input("Enter any number : ") 
          
if choice == 1: 
  print("result = ",add(a,b))      

elif choice == 2: 
  print("result = ",subtract(a,b))           

elif choice == 3: 
  print("result = ",multiply(a,b)) 

elif choice == 4: 
  print("result = ",division(a,b)) 

else :
    print("INVALID CHOICE !!)
