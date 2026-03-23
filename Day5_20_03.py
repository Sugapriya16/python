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


