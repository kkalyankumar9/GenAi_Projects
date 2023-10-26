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


    
   