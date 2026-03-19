import math
import random
#Numeric
#int,float,complex(have real and imaginery)
x =4
y=4.35
z = 2+3j

#Measure a distance 
print (abs(2-10))

#Rounding Numbers
price = 54.667802
print(round(price))
print(round(price,2))
print(math.floor(price))
print(math.ceil(price))
print(math.trunc(price))

#random
print(random.random())
print(random.randint(1,10))
print(random.randrange(12))

#Validation
a=7.0
print(a.is_integer())
x1=12.4
print(isinstance(x1,float))

#Challange
v= random.randint(1,100)
print(v)
print(f"IS Even:", v%2==0)

x =3
y=4
print(divmod(x,y))

#function returning T / F
print(bool(""))
print(bool(0))
print(bool("qet5678u"))

email =""
ph=""
username="sugapriya"
#usecase: check any one field is filled
print(any([email,ph,username]))
#usecase: check all field is filled
print(all([email,ph,username]))

#Logical and conditional operation
#Task1 allow accessonly if user is logged in or they are guest but they must not banned
user ="guest"
result = (user == "guest" or user == "loggedin") and (not user == "banned")
print (F"Task1:" , result)

#Task2 Validate that the domain is not on the banned list
Banned = ["a","d","c","d","g","f"]
domain = 'v'
print(f"Task2:",domain not in Banned)

#Challenges
#No-1 : Check user's name is not empty and age is greater than or equal to 18
UserName = "Sugapriya"
age = 29
Valid_UserName = UserName is not None and UserName != ""
Valid_Age = age >= 18
print(f"ChallengNo-1 : Username is Not Empty:",Valid_UserName," Valid age:",Valid_Age)

#No-2 : Check if the password ia at least 8 char long and does not contains space
password = " ayehfueybjhiedii "
print(f"ChallengNo-2 :Give Password as length moare than 8 and not have space :", (len(password)>8 and " " not in password) )

#No-3 : Check user's email is not empty , contains @ and ends with.com
UserEmail = "Sugapriya@gmail.com"
print(f"User's email is not empty , contains @ and ends with.com :" , UserEmail is not None and UserEmail != "" and
UserEmail.endswith(".com") and "@" in UserEmail)