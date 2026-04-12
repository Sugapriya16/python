#Conditional Statment
score = 55
if score >= 90 :
    if score >=95:
        print("A+")
    else: print("A")
elif score >= 80 :
    print("B")
elif score >= 60 :
    print("c")
elif score >= 50 :
    print("D")
else : print("fail")

#Inline If statement
x=  "A" if (score>=95) else "B"
print(x)


#Match case (Only used for matching Values)
country = "India"
match country:
    case "United States": print("US")
    case "India": print("IN")
    case "Germany": print("GE")
    case _ : print("Unkown Country")

#Challange
email = "@ugapriya.msmail.com  "
#clean string
email = email.strip()
if email =="" or email is None:
    print("Email is empty")
elif (len(email)>254):print("Email should be less than 254 Characters")
elif not (("." in email) and "@" in email ): print("Email should have '.' & '@' Charactes")
elif (email.count("@") !=1) : print("Email should have '@' at once Charactes")
elif not (email.endswith (".com") or email.endswith (".org") or email.endswith (".net")):
     print("Email should endwith '.com','.org','.net'")
elif  not(email[0].isalnum() and email [-1].isalnum()) : 
    print("Email should start and end with alpha and number")
else : print ("Valid Email")

#Challange 2 (Validate password)
email = "Sugapriya@gmail.com"
password = "priyagghgjjh"
if not(password =="" or password is None) and len(password) <8:
    print("Enter a  valid password")
elif (password == email):  print("Passowrd and email should not be same")
elif (" " in password): print("Passowrd should not have space")
elif (password.islower()or password.isupper()) :
    print("Passowrd should capital and small case letters")
elif  not(email[0].isalnum() and email [-1].isalnum()) : 
    print("Password should start and end with alpha and number")
else : print ("Valid password")

#looping
#range(start,stop,step)
for item in range (0,12,3):
    print(f"loop value {item}")

#Challenge
for i in range (1,11):
    print(f"7 x {i} = {i*7}")

for i  in range(7):
       print("*"*i)

#Break =>break the loop
#Continue =>Skip current value
#Pass => Nothing will change (normal segment will continue)

#Else statment in for loop
#IT is used to check loop is completed or breaked 
for i in range (1,10):
    if i%2 == 0:
        print("Even is found")
        break
else: print ("Loop completed")

#Task to find wheather all data files are CSV

files =["data.csv","data2.csv","data3.pdf","data4.csv"]
for file in files :
        if  not (file.endswith(".csv")):
            print ("Not all files are CSV")
            break
else: print ("All data files are CSV")

#Challenge
files = ["data.csv","data2.csv","data3.pdf","data4.csv","data5.csv"]
for i in range(len(files)) :
    for j in range(i+1,len(files)) :
        if (files[i]==files[j]):
            print ("Found duplicate value")
            break
    else: continue
    break
else: print("All files are unique")

files = ["data.csv","data2.csv","data3.pdf","data4.csv","data.csv"]
for i  in range(1 ,len(files)) :
    if (files[0]==files[i]):
       print ("Found duplicate value")
       break
else: print("All files are unique")  

#Use case of Nested loop
#Writing query for tables,columns
tables =["Customer","name","price","orders"]
columns =["id","created_date"]
for t in tables:
    for c in columns:
        print(f"Select * from {t} where {c} is null")

#while loop 
#Challange
count = 0
while (count <3):
    answer = input ("Do you agree (yes/no)")
    if answer == "yes": 
       print("Glad we are on the same page")
       break
    count +=1    
else: print("3 Strikes , You are out")


