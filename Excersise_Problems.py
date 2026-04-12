body = "Boo@  was wonderful* to Read with Beautiful_scripts and actions "

print(f"""@ found at postion  {body.find('@')},
* found at postion  {body.find('*')}, 
_ found at postion  {body.find('_')}""") 

#-----------------------------------------------------------------------------------------------
#1.Given two sorted arrays nums1 and nums2 of size m and n respectively,
#  return the median of the two sorted arrays.
#----------------------------------------------------------------------------------------------

num1 =  list(map(int, input("Enter numbers for 1st list: ").split()))
num2 =  list(map(int, input("Enter numbers for 2nd list: ").split()))
num1.extend(num2)
num1.sort()
print(num1)
median = int(len(num1)/2)
if len(num1) % 2 == 0:    
    print ( "Output :", (num1[median]+num1[median-1])/2)
else : print("Output :",num1[median]) 

#Solution 2
m = int(len(num1)/2)
print(f"Soultion 2 =>Output : { (num1[m]+num1[m-1])/2 if len(num1)%2 ==0 else num1[m] }")

