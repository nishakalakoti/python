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


print("**************practice9*************")

#***************set difine************#
vowels={"a","e","i","O","u"}
print(vowels)
#find e to vowels
charvowels = "e" in vowels
print("e in vowels ", charvowels)

# find in vowels
charvowels= "w" in vowels
print("w in vowels ", charvowels)

print("**************practice10*************")

#*********using dictionary*******#
dictionary = {
          "name": "nisha",
          "age": 22,
          "grades": [85]
        }
print(dictionary)
dictionary["age"] = 23

dictionary["favoritesubject"] = "Mathematics"
print(dictionary)




print("**************practice11*************")

cities_and_their_populations={

                               "New York": 8419600,
                             "Los Angeles": 3980400,
                              "Chicago": 2716000,
                                "Houston": 2328000,
                              "Phoenix": 1690000,
   }
print(cities_and_their_populations)
chicago_population = cities_and_their_populations.get("Chicago")
print(f"Population of Chicago: {chicago_population}")

removedpopulation =cities_and_their_populations .pop("Los Angeles")
print(f"Removed Los Angeles, population was: {removedpopulation}")



print("**************practice12*************")


countriesinfo = {
    'India': {'capital': 'New Delhi', 'population': 1393409038},
    'Brazil': {'capital': 'Brasília', 'population': 213993437},
    'USA': {'capital': 'Washington D.C.', 'population': 331449281},
    'China': {'capital': 'Beijing', 'population': 1444216107},
    
}

capital_India = countriesinfo['India']['capital']
print(f"The capital of India is: {capital_India}")

countriesinfo['Brazil']['population'] = 332915073  
print("\nFinal dictionary after updates:")

print(countriesinfo)




