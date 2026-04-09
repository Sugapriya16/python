import copy
#Data Structure

#List => Collection of objects where pointers of list of varaible stored
#One dimentional
letters= list("Python")
print(letters)

numbers = list(range(5))
print(numbers)

mixedlist = [1,'a',True,None]
print(mixedlist)

#Matrix
#More dimentional

matrix =[[1,2,3,4],
          [6,8,7,9]]
print(matrix)

mixedmatrix =[['q','e','r'],[1,2,3,4],[True,False]]
print(mixedmatrix)

#Access and Read

stringlist = [["Love"],
              ["India"],
              ["Country","Sugapriya"]]

#Indexing
#Last row
print(stringlist[-1])
#Last element
print(stringlist[-1][-1])
#Last letter
print(stringlist[-1][-1][-1])

#Slicing
lst =['a','b','c','d']
print(lst[2:3])
print(lst[2:])
print(lst[:-1])

matrix2 =[[2,3,4,5],
        [5,6,7,8,9],
        [0,1,2,23,45]]
print(matrix2[:2])
print(matrix2[1][:2])

#Change the existing list
lst.append(2)#add one element
print(lst)
matrix2.append([1,2,3,4])
print("Matrix after append one row:", matrix2)
matrix2[1].append(8)
print("Matrix after append one element in 2nd row:", matrix2)
lst.extend([2,3])#add multiple element
print(lst)
lst.insert(2,'w')
print(lst)
lst.remove(2)#remove by value
print(lst)
lst.pop()
print(lst)#remove last index
lst.pop(3)
print(lst)#remove by index

#Challange 
#Get the last element from the list	
a = ["QA", "Automation", "Testing"]
print(f"Challange 1 => Last element in list: {a[2]}")
#Get the first character of "Automation"	a = ["QA", "Automation", "Testing"]
print(f"Challange 2 => First character of Automation: {a[1][0]}")
#Get the last 3 characters of "Testing"	
print(f"Challange 3 => last 3 characters of Testing: {a[2][-3:]}")
#Reverse the string "Automation"
b = a[1][::-1]
print(f"Challange 4 => Reverse the string Automation {b}")

#Unpacking list
#Unpacing rules => No of varaiables are matching with values
person = ["Sugapriya",29,"Data Engineer","Chennai","India"]
name,age,role,city,country= person
print(name,age,role,city,country)
#Rest Collection (Asterik*)
name ,*detail,country = person
print(name)
print(detail)
print(country)

# place a _ if we are not taking a value (Not giving a variable to store)
data =["Sugapriya","Data Engineer","29","single","chennai","India"]
name,role,_,_,*Location = data
print(name)

#Explore and Analyze
num = [1,2,3,4,5,2,4,2,2,6]
print(min(num))
print(max(num))
print(sum(num))
print("Length :",len(num))

print("Is all value are present in list :",all(num))
print("Is all value are present in list :",all([1,0,3]))
print("Is all value are present in list :",all(['a','','b']))

print("Is any one value are present in list :",any(num))
print("Is any one value are present in list :",any([1,0,3]))

print("Count:",num.count(2))
print("Count:",num.index(2))
 
data2 =[2,3,4]
data3=[2,3,4]

print( "Compare 2 list :", data2==data3)#compare th evalue
print( "Compare 2 list :", data2 is data3)#Compare the memory

#sorting
data=[3,4,1,2,34,5,6,8,1,2,34,5]
data.sort()
print("SortedData :",data )
data.sort(reverse = True)
print("Reverse SortedData :",data )
matrix = [['d','s','d','g'],
          ['s','d','f','r'],
          ['a','e','r','t']]
matrix.sort()
print("Sorted  Matrix: ", matrix) #sorted by 1st element in a row
matrix[1].sort()
print("Sorted  2nd row in Matrix: ", matrix) #sorted 2nd row 

#making extra varaible to store
dlist =[1,4,5,2,3]
sdlist = sorted(dlist)
print(sdlist)
dlist.reverse()#swaping 1st and last
print(dlist)
rdlist = list(reversed(dlist))
print(rdlist)

#Coping
lst=['2','3','4','5']
#1.Assignment
cplst = lst #same list and memory sharing 
cplst.append('f')
print(lst)
#2.Shallow copy
cplst = lst.copy()
cplst.extend(['2','4','5'])
print("Orignal:",lst,"Copied :",cplst)

matrix3 = [[2,3,6,7],
        [2,3,4,6,9]]
cmatrix3=matrix3.copy()
cmatrix3[1].append("z")
print("Orignal:",matrix3,"Copied :",cmatrix3)#It will affect the original list
#where its shallow copy : Copy 1st level of object who share the memory
dcmatrix3=copy.deepcopy(matrix3)#Copy all the level of data
dcmatrix3[1].append("y")
print("Orignal:",matrix3,"Deep Copied :",dcmatrix3)
#copy.copy(dcmatrix)=>is as shallow copy
#copy() function can use only in list
#for another data type need use copy.copy() after importing copy class

#combining
letters = ['a','b','c','d']
numbers =[1,2,3,4]
comb =letters+numbers
print("Combining using '+' symbol:" , comb)#Creating a new varaiable
print("Multiplying list :" , letters*2)
comb = [letters,numbers]
print("Combining as matrix:", (comb))
letters.extend(numbers)
print("Combining using extending adding a list at end :",letters)

#Using Zip (reult always in tuples format)
ids =[123,124,125,126,127]
names =['Suga','Priya','Viki','Moni','Karthi']
print("Comabined using zip function :", list(zip(ids,names)))

#Iteration
letters = ['s','d','f','g']
for i in letters:
     print(i)
for index,value in enumerate(letters):
    print(f"Printed using enumerate loop :index - {index}, value - {value}")
for i in reversed(letters):
    print("Created reversed list :",i)
for l,n in zip(letters,numbers):
    print ("Itersted to Zip tuple after comabined two list :" , l ,n)
#map(transformation,list variable)
print("Using map transformed list:", list(map(str.upper,letters)))
for i in map(str.upper,letters):
    print ("Iterated to map output :",i)

#Filtering
data4 =['fog','122']
for i in filter(str.isalpha,data4):
    print("Using fileter removing data form list :",i)

#Lambda
multiple = lambda x:x*2
print("Using lambda:" , multiple(4)) 
add = lambda x,y,z : x+y+z
print("Using Lambda :" ,add(3,4,5))

#Map & Lambda
#Change all string to float
prices = ['$45.3','$23.2','$56.3','$78.2']
print(list(map(lambda p :float(p.replace("$",'')), prices)))

# Lambda & filters
prices =[123,45,124,100,34,165]
print( list (filter (lambda p:p>=100,prices)))

students = [['Maria',85],
            ['Suga',87],
            ['Priya',67],
            ['Max',50]]
print(list(filter (lambda row : row[1]>=70 ,students)))

#Challange to get students with name strats with 'M'
print(list(filter(lambda row:row[0].startswith('M'),students)))

#List Comprehension
#=> Data transformation,Data Loop and Data filter
#Task for cleaning a domain list
domains =['www.google.com',
'openai.com','localhost',
'WWW.DATAWITHBARAA.COM']

cleaned = [
    #1st =>Data Transformation
    d.lower().replace("www.",'')
    #2nd =>Data loop
    for d in domains
    #3rd =>Data filtering (Optional)
    if '.' in d
]
print("Output of Comprehension: ", cleaned)

#Tuple
#Unmutable
tupledata = (1,2,3,4)
for i in tupledata:
    print("TupleData: ",i)
d = sorted(tupledata)
print(d)#Changed to list

#Set
setdata ={2,23,11,12,24,10,2}
print("Data Set :",setdata)#duplicates will remove
#Not indexed
setdata.remove(10)#remove (will  return error if there is no value)
print("Data Set after remove:",setdata)
#Update set
setdata.add(1)#add only one value
print("Data Set after add:",setdata)
setdata.update([3,4,5])#more values, any data type
print("Data Set after update:",setdata)
setdata |= {0,9}
print("Data Set after update symbol:",setdata)
#discard(will not return error if there is no value)
setdata.discard(9)
print("Data Set after discard :",setdata)
      
#Mathamatical opersation in sets
a ={10,12,13,14,15,30,40}
b= {10,90,40,13,24,50,8,7}
#Union
print("Union Operator :", a.union(b))
print("Union Symbol :", a | b)
#Intersection
print("Intersection Operator :", a.intersection(b))
print("Intersection Symbol :", a & b)
#Difference
print("Difference Operator :", a.difference(b))
print("Difference Symbol :", a - b)
print("Difference Symbol :", b - a)
#Symentric_difference
print("Symentric_Difference Operator :", a.symmetric_difference(b))
print("Symentric_Difference Symbol :", a ^ b)

#Set-Relationship methods
c={10,20,30}
d={20,30,40,50,10}
print("Checking c is subset of d:", c.issubset(d))
print("Checking d is superset of c:", d.issuperset(c))
print("Checking c and d doesn't have any common :" , d.isdisjoint(c)) 

#Dictionary
user ={"Name":"Sugapriya","Age":29,"City":"Bangalore"}
#Access
print(user.get("Name"))
#Check (Keys are present)
print("Age" in user)
#View Objects
print(user.keys())
print(user.items())#Returns list of tupls
print(user.values())
print(user)
#Looping
for key,value in user.items():
    print(key,value)
#Update
user["id"]=1
user.update({"state":"Karnataka","Date":"22/4/2026"})
print("After update :",user)
#pop
user.popitem()
print("After POP last item :",user)
user.pop("id")
print("After POP given key:",user)
#Creation 
user = dict.fromkeys(["id","name","age","city","dob"],None)
print("User list after creating with fromkeys:",user)

#Challange : Keep only string values & convert them to uppercse
user ={"id": 1,"name":"John","age":30,"city":"Berlin"}
#Using compension 
user_str ={
    k: v.upper()    #Expression
    for k,v in user.items() #Loop
    if isinstance(v,str)#Filtet
}
print(user_str)