built int functions to convert type of variables:
int() e.g. 1
float() e.g. 1.1
bool() e.g. True
str() e.g. 'a'



age = 20
first_name = input("Type name: ")
last_name = input("Type last name: ")
patient = "New Patient"

if first_name == "John" and last_name == "Smith":
    print(first_name, last_name, "Age:", age, patient)
else:
    print("User does not exist")


name = input("What is your name? ")
print("Hello " + name)

birth_year = input("Enter your birth year: ")
age = 2021 - int(birth_year)
print(age)


#calculator:
firstValue = input("Enter First Value: ")
secValue = input("Enter Second Value: ")
sum = float(firstValue) + float(secValue)
print("Sum: " + str(sum))

#strings: course.# functions are specific to strings 
course = "Python for begginers"
print(course.replace('for', '4'))

print("Python" in course)

#Arithmetic Operators
print(10 + 3)
print(10 / 3)
print(10 // 3)
print(10 % 3)
#** means power of #
print(10 ** 3)
x = 10
x = x + 3
#augemnted operator:
x += 3


#Comparison operators:>; <; >=; <=; ==(equal); !=(not equal)
x = 3 > 2


#Logical operators:
and (both)
or (at least one)
not (inverts any given value)

price = 5
print(price > 10 or price < 30)
print(not price > 10)


#If Statements: 
temperature = 10
if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20:
    print("It's a nice day")
else:
    print("Go get some clothes")


#While Loops: to loop block of codes multiple times
i = 1
while i <= 5:
    print(i)
    i = i + 1

i = 1
while i <= 10:
    print(i * '*')
    i = i + 1


#Lists. We add lists to []
names = ["John", "Bob", "Pov", "Sam", "Mary"]
names[1] = "Bab" #Modify item of the list
print(names[0:3]) #Print only selected items. Creates a NEW list!
print(names)


#List methods
number = [1, 2, 3, 4, 5,]
number.remove(3)
print(number)

number = [1, 2, 3, 4, 5,]
print(1 in number)

number = [1, 2, 3, 4, 5,]
print(len(number))


#for loops: print each item in a separate line
number = [1, 2, 3, 4, 5,]
for item in number:
    print(item)
#the same can be acchieved with: while, but it's much longer
i = 0
while i < len(number):
    print(number[i])
    i = i + 1


#range function (to generate sequence of numbers)
numbers = range(5, 10, 2)
for number in numbers:
    print(number)

for number in range(5):
    print(number)


#Tuples: Like a lists, used to store sequence of objects. Tuples are immutable (cannot be chaanged)
numbers = (1, 2, 3, 3)
numbers.count(3)