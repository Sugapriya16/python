# String Datatype
#types
a ='adb'
print (type(a))
b=10
print (type(10))
print (type(str(b))) #converting int to str

#Math
c = 'qww234dcf'
print(len(c))
d ='qwedvqchsnweaqsqndq'
print (d.count('q'))

#transformation
#str.replace(old, new, /, count=-1)
phone = "123-456-789"
print(phone.replace("-", " "))
print(phone.replace("-", " ",1))

#Challange
phoneNo = '+49 (179) 123-4567'
#chain commend from left to right
print(phoneNo.replace(" ","").replace("+","00").replace("(","").replace(")","").replace("-",""))

#f String
name ='sugapriya'
salary ='35'
is_data_engineer = True
print (f"My name is {name}, salary {salary}, is my role is data engineer {is_data_engineer}")

csvfile = "123,max,USA,2026-03-16,635801"
print(csvfile.split(",")) # storing as list

print( "#" * 30)

#Indexes and Slicing 
#syntax variable[startindex: endindex-1]
date = "2026-03-16"
# Extract year, month & date
year = date [:4]
month = date [5:7]
date = date[-2:]
print (f"year : {year} , month :{month}, date: {date}")

#cleaning
data = " Engineering "
print (data.strip())
data2 = "###ASD####"
print (data2.strip("#"))

#Case Conversions
search = " EMail".lower().split()
data3 = "email".lower().split()
print(search==data3)

#Challange
messyStr = "968-Maria , ( D@t@ Engineer ) ;; 27y   "
messyStr=messyStr.lower().strip()
messyStr = messyStr.replace("@","a")
print(f"Name : {messyStr[4:9]}, Role : {messyStr[13:27]}, age: {messyStr[-3:-1]}")

#Search
Phone = "+48-234-23456"
print(Phone.startswith("+49"))
#str.endswith(suffix[, start[, end]])
email = "sugapriuams16@gmail.com"
print(email.endswith("outlook.com"))
print (email.endswith('16',0,email.find('@'))) #optional start or  optional end
print('@' in email)
print(Phone.find('-'))
print(Phone[Phone.find('-')+1: ])

#String Methods
#str.center(width, fillchar=' ', /)
value = 'python'
print(value.center(15,'#'))

#str.split(sep=None, maxsplit=-1)
splitval = "1,2,,2,2,,,"
print(splitval.split(",",maxsplit=3))

#str.swapcase()
swapvalue = "dfetvSSsfU"
print(swapvalue.swapcase())


#Validation
country = "india"
print(country.isalpha())
phone ="234"
print(phone.isnumeric())
print("/".join(phone))