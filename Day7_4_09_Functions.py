#Functions
import math

#Bulit-in Function
print(len('python'))#Just Call

#Function from Libararies 
#Need to import and call
print(math.ceil(4.2))

#User Defined Function (Create function and call)
def greet():
    print("Hello inside the user defined function")

greet() # Function call

#Parameters and Functions
def clean_word(name): # Inside bracket is parameter
    print(name.strip().lower())
clean_word("  PRiya ")#Inside bracket is argument

#Global and Local Variable
#GV => Created outsie the function all can access
#LV => Created inside the function  inside function only able to access
Case_rule ="Clean all space"
def clean_word(name,age="0",married="no"): #Parameter
    Case_rule # Global Variable
    Cleaned = name.strip().lower() #Local Variable
    print(f"Name :{Cleaned}  and age : {age} and married {married}")

#Arguments type
#=> Positional Arguments
clean_word("  PRiya ",29)#Inside bracket is Arguments
#=> Keyword Arguments
clean_word(age =30,name ="  PRiya ")
#=> Mixed Arguments
clean_word("  PRiya ",age=10)

#Default parameter
#=>giving value in absence of argument
clean_word("  RiYA ")

#if we not aware of numer of arguments use *args
def total(*args):
    print("Total: " ,sum(args)) # where args is tuple type
total()
total(1,2,3,5,7)
total(1,2,4)

#Return type function

def clean_name (name):
    up_case = name.strip().upper()
    lo_case = name.strip().lower()
    return up_case,lo_case

UP_Name, LO_Name = clean_name("maRiA")
print(f"Upper Case name {UP_Name}, Lower Case name {LO_Name}")


#Action Function
#Task : Store application message in a file
def writelog(message):
    with open(r"D:\Python_Learning\Learning Files\log.txt","a") as file:
       file.write(message + "\n")

writelog("Start App")
writelog("User Logged In  and Logged Out")
writelog("App Closed")

#Transformation function
#Task : Clean a email and split into user name and domain
def clean_email (email):
    email.strip().lower()
    data = email.split("@")
    print(f"Username : {data[0]} and domain : {data[1]}")

clean_email(" sugapriyams16@gmail.com ")

def clean_split_email(email):
     email = email.strip().lower()
     username , domain = email.split("@")
     return {"UserName" : username,
     "Domain": domain}
print(clean_split_email(" VigNesh@Gmail.com"))

#Validation function

def Is_Password_valid(password):
    """Used to valid the password"""
    return len(password)>9 
print(f"Password is valid: {Is_Password_valid('Suga112340')}")

def Is_Email_Valid(email):
      return "@" in email and "." in email

#Orchestrator Function(Work flow function)
#Mini Project
# Receive an email from the user
# Validate the email
# If it is invalid, log an error in a file
# If it is valid, clean and structure the email
# Log each step of the program

#Function rules
# => 1. Always use snake_case for naming eg:div_call
# => 2. User clear descriptive name mostly start with verb avoid abberivations eg:calculate_discount
# => 3. Check the parameter name should be in fullform easy to understand by team people
# => 4. Use Docstring at 1st like of function explaining what the function does
      """ Eg: Use of the function instead of # we using this because 
      Python will ingonre it when we give discribtion like this it will return in ide as below"""
help(Is_Password_valid)
# => 5. Use return instead of print
# => 6. Give hint for parameter datatype eg: sum ( a: int , b: int) -> float : (retrun value data type)