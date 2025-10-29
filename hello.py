
#import numpy as np


# variable_name=data
"""
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello, " + name + "!" + " You are " + age + " years old.")
"""
"""
#lists
foods = ["pizza", "burger", "pasta", "salad"]

#tuples
dimensions = (1920, 1080)

#dictionaries
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

#sets
unique_numbers = {1, 2, 3, 4, 5}
"""

#checking data types
#print(type(name))
"""
is_student = True
print(type(is_student))

food = "pizza"
print(type(food))

print(isinstance(food, str))
print(isinstance(False))
print(isinstance(456, bool))
print(isinstance(True, bool))
print(isinstance(3.14, float))
"""

#name = "Alice"
#print(name)
#age = 56
#print(age)
"""
list=[1,2,3,4,5]
print(list)

list2=["Red", "Blue", "Green"]
print(list2)

list3=[True, False,] #boolean
print(list3)

list4=["Nato", 1,2,3,4,5, True, False] #mixed
print(list4)

list5=[] #empty list
print(list5)

list6=list5.append("Hello") #adding to list
print(list5)
print(list6) #prints None because append() modifies the list in place and returns None

list7=list4.append("world")
print(list4)

list4.extend(list3) #adding multiple items to list
print(list4)
list4.pop() #removing last item
print(list4)
list4.remove("Nato") #removing specific item
print(list4)
list4.insert(0, "Nato") #inserting item at specific index
print(list4)
print(list4[0]) #accessing item by index
print(list4[1:4]) #slicing list
"""
#Asking a random and getting a random answer from the ones provided
"""

import random
ans = ["yes - definately", "it is decidely so", "without a doubt", 
"reply hazy", "try again later", "my sources says no", "outlook not so good",
"very doubtful."]
question = input("Type your question below:")
random_ans=random.choice(ans)
print(f"Answer: {random_ans}")


#a simple program that uses combination of relation and logical operations and rules
height = int(input("Enter your height below: "))
credits = int(input("Enter your credits below: "))

if height >= 5.5 and credits >= 15:
  print("Enjoy the ride!")
elif height < 5.5 and credits >= 15:
  print("You are not tall enough to ride. ")
elif height >= 5.5 and credits < 15:
  print("You do not have enough credits")
else:
  print("You have not met the requirements, sorry.")
"""
  #string interpolation
n_bottles = 99
for n in range(n_bottles, -1, -1):
  print(f"{n} Bottles of beer on the wall.")
  print(f"{n} Bottles of beer")
  print("Take one down, pass it arround")
  print(f"{n-1} Bottles of beer left on the wall.\n")

#Getting numbers from 0 to 100 but multiples of 3 will output "fizz" while those of 5 will output "Buzz" and those of both 5 and 3 will output "fizzBuzz"
for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print("FizzBuzz")
  elif i % 3 == 0:
    print("Fizz")
  elif i % 5 == 0:
    print("Buzz")
  else:      
    print(i) 

def is_aldult(age):
  if age > 18:
    return True
  else:
    return False
  #using ternary operator
def is_adult2(age):
  return True if age > 18 else False  
      
#Dictionaries
dog = {"name": "Roger", "age": 8}
#print(dog["name"])      
      
  #Notes on loops
    
#for loops
""" for i in range(5): #0,1,2,3,4
  print(i) #prints numbers from 0 to 4"""
""" for i in range(1, 6): #1,2,3,4,5
  print(i) #prints numbers from 1 to 5"""
""" for i in range(1, 11, 2): #1,3,5,7,9
  print(i) #prints odd numbers from 1 to 10"""
""" for i in range(10, 0, -1): #10,9,8,7,6,5,4,3,2,1
  print(i) #prints numbers from 10 to 1"""
""" for i in range(5):
  print("Hello") #prints Hello 5 times"""
""" for i in range(1, 6):
  print("Hello " + str(i)) #prints Hello 1, Hello 2, Hello 3, Hello 4, Hello 5"""
""" for i in range(1, 6):
  print(f"Hello {i}") #prints Hello 1, Hello 2, Hello 3, Hello 4, Hello 5"""
#while loops
""" count = 0
while count < 5:  #while count is less than 5
  print(count) #prints count
  count += 1 #increments count by 1"""
""" count = 1
while count <= 5:  #while count is less than or equal to 5
  print(count) #prints count
  count += 1 #increments count by 1"""
""" count = 5
while count > 0:  #while count is greater than 0
  print(count) #prints count
  count -= 1 #decrements count by 1"""
""" count = 1
while count <= 5:  #while count is less than or equal to 5
  print("Hello " + str(count)) #prints Hello 1, Hello 2, Hello 3, Hello 4, Hello 5
  count += 1 #increments count by 1"""
""" count = 1
while count <= 5:  #while count is less than or equal to 5
  print(f"Hello {count}") #prints Hello 1, Hello 2, Hello 3, Hello 4, Hello 5
  count += 1 #increments count by 1"""
#nested loops
""" for i in range(1, 4): #outer loop
  for j in range(1, 4): #inner loop
    print(f"i: {i}, j: {j}") #prints i: 1, j: 1, i: 1, j: 2, i: 1, j: 3, i: 2, j: 1, i: 2, j: 2, i: 2, j: 3, i: 3, j: 1, i: 3, j: 2, i: 3, j: 3"""
""" for i in range(1, 4): #outer loop
  for j in range(1, 4): #inner loop
    print(i * j) #prints multiplication table"""
#break and continue
""" for i in range(1, 11):
  if i == 6:
    break #exits the loop when i is 6
  print(i) #prints numbers from 1 to 5"""
""" for i in range(1, 11):
  if i == 6:
    continue #skips the iteration when i is 6
  print(i) #prints numbers from 1 to 10 except 6"""
#example program to find the sum of squares of first n natural numbers
"""number = int(input("Enter the number you would like to find it\'s square: "))"""
number = 5
total = 0
square = number ** 2
for i in range(1, number +1):
    total += i * i
print(total)

#functions notes
"""
def greet(name):
  print(f"Hello, {name}!") #prints Hello, name!
greet("Alice") #calls the function with argument "Alice"
greet("Bob") #calls the function with argument "Bob"
"""
"""
def add(a, b):
  return a + b #returns the sum of a and b
result = add(3, 5) #calls the function with arguments 3 and 5
print(result) #prints 8
"""
"""
def factorial(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * factorial(n - 1) #recursive call
print(factorial(5)) #prints 120
print(factorial(0)) #prints 1
print(factorial(1)) #prints 1
"""
""" def is_even(n):
  return n % 2 == 0 #returns True if n is even, False otherwise
print(is_even(4)) #prints True
print(is_even(5)) #prints False
"""
""" def fibonacci(n):
  if n <= 0:
    return []
  elif n == 1:
    return [0]
  elif n == 2:
    return [0, 1]
  else:
    fib_seq = [0, 1]
    for i in range(2, n):
      next_fib = fib_seq[i - 1] + fib_seq[i - 2]
      fib_seq.append(next_fib)
    return fib_seq
print(fibonacci(10)) #prints first 10 Fibonacci numbers
print(fibonacci(0)) #prints []
print(fibonacci(1)) #prints [0]
print(fibonacci(2)) #prints [0, 1]
"""