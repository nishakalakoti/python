print("**************practice1*************")

# ********* tuple**********#

numbers=[1,2,3,4,5,6,7,8,9,10]
squre=[x**2 for x in numbers]
print(squre)

my_tuple=[1,2,3,4,5,6,7,8,9,10]
my_tuple[3]=50
print(my_tuple)


my_tuple=[1,2,3,4,5,6,7,8,9,10]
my_tuple[3]=50
my_tuple[5]=25
print(my_tuple)


numbers=[1,2,3,4,5,6,7,8,9,10]
numbers.remove(10)
print(numbers)






print("**************practice2*************")

#************fumction to number and char*************#

naturalnumbers={1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20}
print(naturalnumbers)
my_tuple={1,2,3,4,5,6,7,8,9,10,}
a,b,c,d,e,f,g,h,i,j=my_tuple
print(a,b,c,d,e,f,g,h,i,j,)
print(a,b,c,d,e)



print("**************practice3*************")

#**********using formula squre and odd numbers*********#

oddnumbers = [x for x in range(1, 20, 2)]
squaredoddnumbers = [x**2 for x in oddnumbers]

print("Odd Numbers", oddnumbers)
print("Squares of Odd Numbers", squaredoddnumbers)






print("**************practice4*************")

#***********type effect*************#

continents = ("nisha", "tannu", "vimal", "rahul", "gita")
print(continents[2]) 
try:
    continents[1] = "poonam"  
except TypeError as e:
    print(f"Error: {e}")  
    print( continents[1])




print("**************practice5*************")

#**********using tupal num,word,float **********#

my_tuple = ("nisha", 22, 6.43)

string_variable, int_variable, float_variable = my_tuple

print("String:", string_variable)
print("Integer:", int_variable)
print("Float:", float_variable)




print("**************practice6*************")
#************tuple function to number and char it's colled nested tuple*************#

myy_tuple={1,2,3,}
a,b,c=myy_tuple
print(b)
myy_tuple={4,5,6,}
d,e,f=myy_tuple
print(d)



print("**************practice7*************")

#**********using set **********#


setoddnumbers={x for x in range(1, 10, 2)}
print(setoddnumbers)
setevennumbers = {x for x in range(1, 12) if x % 2 == 0}
print(setevennumbers)
#union
setoddnumbers={x for x in range(1, 10, 2)}
setevennumbers = {x for x in range(1, 12) if x % 2 == 0}
data=setoddnumbers.union(setevennumbers )
print(data)
#intersection
setoddnumbers={x for x in range(1, 10, 2)}
setevennumbers = {x for x in range(1, 12) if x % 2 == 0}
data=setevennumbers.intersection(setoddnumbers)
print(data)


print("**************practice8*************")

primenumbers={1,2,3,7,13}
print(primenumbers)
#   adding element
primenumbers.add(11)
print(primenumbers)
#  removing element
primenumbers.remove(2)
print(primenumbers)
# checking number to set
sevennumber = 7 in primenumbers
print("7 in set ", sevennumber)








