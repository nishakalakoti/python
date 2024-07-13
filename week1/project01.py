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