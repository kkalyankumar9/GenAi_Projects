str="hello world"
print(str)
# Integer
integer_variable = 10

# Float
float_variable = 3.14

# String
string_variable = "Hello, World!"

# Boolean
boolean_variable = True

# List
list_variable = [1, 2, 3, 4, 5]

# Tuple
tuple_variable = (1, 2, 3, 4, 5)

# Dictionary
dictionary_variable = {"name": "Alice", "age": 30}

# Set
set_variable = {1, 2, 3, 4, 5}

# Print types and values
print(f"Type of integer_variable: {type(integer_variable)}, value: {integer_variable}")
print(f"Type of float_variable: {type(float_variable)}, value: {float_variable}")
print(f"Type of string_variable: {type(string_variable)}, value: {string_variable}")
print(f"Type of boolean_variable: {type(boolean_variable)}, value: {boolean_variable}")
print(f"Type of list_variable: {type(list_variable)}, value: {list_variable}")
print(f"Type of tuple_variable: {type(tuple_variable)}, value: {tuple_variable}")
print(f"Type of dictionary_variable: {type(dictionary_variable)}, value: {dictionary_variable}")
print(f"Type of set_variable: {type(set_variable)}, value: {set_variable}")


# problem 3
# Create a list of numbers from 1 to 10
numbers_list = list(range(1, 11))

# Add a number to the list
numbers_list.append(20)

# Remove a number from the list
if 5 in numbers_list:
    numbers_list.remove(5)

# Sort the list
numbers_list.sort()

# Print the updated list
print(numbers_list)

# problem 4
# 4. **Sum and Average**: Write a Python program that calculates and prints the sum and average of a list of numbers.
#     - *Input*: [10, 20, 30, 40]
#     - *Output*: "Sum: 100, Average: 25.0"
arr=[10,20,30,40]
sum=0
for i in arr:
    sum+=i
    
print(sum/len(arr))

# 5. **String Reversal**: Write a Python function that takes a string and returns the string in reverse order.
#     - *Input*: "Python"
#     - *Output*: "nohtyP"
st="python"

reve_str="".join(reversed(st))

print(reve_str)
# 6. **Count Vowels**: Write a Python program that counts the number of vowels in a given string.
#     - *Input*: "Hello"
#     - *Output*: "Number of vowels: 2"

st="Hello"
count=0
for i in st:
    if i=="a" or i=="e" or i=="i" or i=="o"or i=="u":
        count+=1
        
print(count)
# 7. **Prime Number**: Write a Python function that checks whether a given number is a prime number.
#     - *Input*: 13
#     - *Output*: "13 is a prime number."
n = 13

# Check if the number is prime
if n > 1:
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            print(f"{n} is not a prime number")
            break
    else:
        print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")

# 8. **Factorial Calculation**: Write a Python function that calculates the factorial of a number.
#     - *Input*: 5
#     - *Output*: "Factorial of 5 is 120."
n=5
factorial=1
for i in range( 1 , n+1):
    factorial*=i
    
print(factorial)

# 9. **Fibonacci Sequence**: Write a Python function that generates the first n numbers in the Fibonacci sequence.
#     - *Input*: 5
#     - *Output*: "[0, 1, 1, 2, 3]"
def fibonacci(n):
    fib_sequence = []
    a, b = 0, 1
    
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
        
    return fib_sequence

# Example usage
n = 5
result = fibonacci(n)
print(result)



# 10. **List Comprehension**: Use list comprehension to create a list of the squares of the numbers from 1 to 10.
#     - *Input*: None
#     - *Output*: "[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]"
# Using list comprehension to generate a list of squares of numbers from 1 to 10
squares_list = [i**2 for i in range(1, 11)]

# Printing the output
print(squares_list)

### Problem **1: Print the following pattern**

# Write a program to print the following number pattern using a loop.
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5

n=5
bag=""
for i in range(1,n+1):
    bag+=str(i)+" "
    print(bag)
    
    ### Problem **2: Display numbers from a list using loop**

# Write a program to display only those numbers from a [list](https://pynative.com/python-lists/) that satisfy the following conditions

# - The number must be divisible by five
# - If the number is greater than 150, then skip it and move to the next number
# - If the number is greater than 500, then stop the loop

numbers = [12, 75, 150, 180, 145, 525, 50]

for num in numbers:
    if num % 5 == 0 and num <= 150:  # Check if the number is divisible by 5 and less than or equal to 150
        print(num)
    elif num > 150:  # Skip the number if it is greater than 150
        continue
    elif num > 500:  # Stop the loop if the number is greater than 500
        break

### Problem **3: Append new string in the middle of a given string**

# Given two strings, `s1` and `s2`. Write a program to create a new string `s3` by appending `s2` in the middle of `s1`.
s1 = "Ault"
s2 = "Kelly"
b1=""
b2=""
for i in range(0,len(s1)//2):
    b1+=s1[i]
for i in range(len(s1)//2,len(s1)):
    b2+=s1[i]
print(b1+s2+b2)

### Problem **4: Arrange string characters such that lowercase letters should come first**

# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.

str1 = "PyNaTive"
b1 = ""
b2 = ""

for i in str1:
    if i.islower():
        b1 += i
    else:
        b2 += i

print(b1 + b2)

### Problem **5: Concatenate two lists index-wise**

# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.



list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3 = []

# Iterate through the indices of the shorter list
for i in range(min(len(list1), len(list2))):
    # Concatenate corresponding elements from list1 and list2
    merged_string = list1[i] + list2[i]
    # Append the merged string to list3
    list3.append(merged_string)

print(list3)

# Problem 6: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
list3 = []

# Iterate through the indices of the shorter list
for i in range(min(len(list1), len(list2))):
    # Concatenate corresponding elements from list1 and list2
    merged_string = list1[i] + list2[i]
    # Append the merged string to list3
    list3.append(merged_string)

print(list3)

### Problem **7: Iterate both lists simultaneously**

# Given a two Python list. Write a program to iterate both lists simultaneously and display items from list1 in original order and items from list2 in reverse order.
list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]


for i in range(min(len(list1), len(list2))):
    b1=str(list1[i])+ " " +str(list2[i])
    print(b1)
# Problem 8: Initialize dictionary with default values

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}

obj={}
for emp in employees:
    obj[emp]=defaults.copy()
    
print(obj)

### Problem **9: Create a dictionary by extracting the keys from a given dictionary**

# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# **Given dictionary**:
# Given nested tuple
tuple1 = (11, [22, 33], 44, 55)

# Convert the list inside the tuple to a mutable list
list_inside_tuple = list(tuple1[1])

# Modify the first item in the list to 222
list_inside_tuple[0] = 222

# Convert the modified list back to a tuple
modified_tuple = (tuple1[0], list_inside_tuple, tuple1[2], tuple1[3])

print(modified_tuple)
