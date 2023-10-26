# Problem.1

people = [("John", 25), ("Jane", 30)]
# Iterate through the list and print each name and age
for i in people:
    name,age=i # Tuple unpacking
    print(f"{name} is {age} years old")

# Problem.2
# Initialize an empty dictionary
people = {}

# Function to add a new name-age pair to the dictionary
def add_person(name, age):
    people[name] = age

# Function to update the age of a person in the dictionary
def update_age(name, new_age):
    if name in people:
        people[name] = new_age

# Function to delete a person from the dictionary
def delete_person(name):
    if name in people:
        del people[name]

# Initial empty dictionary
print("Initial Dictionary:", people)

# Add a new name-age pair
add_person("John", 25)
print("After Adding 'John':", people)

# Update the age of a name
update_age("John", 26)
print("After Updating 'John' Age to 26:", people)

# Delete a name from the dictionary
delete_person("John")
print("After Deleting 'John':", people)

# 1. **Two Sum Problem**: Given an array of integers and a target integer, find the two integers in the array that sum to the target.
#     - *Input*: [2, 7, 11, 15], target = 9
#     - *Output*: "[0, 1]"
def two_sum(nums, target):
    num_indices = {}  # Dictionary to store indices of numbers
    
    for index, num in enumerate(nums):
        complement = target - num
        
        # If the complement is in the dictionary, return its index and current index
        if complement in num_indices:
            return [num_indices[complement], index]
        
        # Store the current number and its index in the dictionary
        num_indices[num] = index
    
    # If no solution is found, return an empty list
    return []

# Input list and target value
nums = [2, 7, 11, 15]
target = 9

# Find the indices of two numbers that add up to the target
result = two_sum(nums, target)

# Output the result
print(result)
# 1. **Palindrome Check**: Write a Python function that checks whether a given word or phrase is a palindrome.
#     - *Input*: "madam"
#     - *Output*: "The word madam is a palindrome."

st3="madam"
bag=""
for i in st3:
    bag=i+bag

if bag==st3:
    print(f"The word {st3} is a palindrome.")
else:
     print(f"The word {st3} is not a palindrome.")

# 1. **Selection Sort**: Implement the selection sort algorithm in Python.
#     - *Input*: [64, 25, 12, 22, 11]
#     - *Output*: "[11, 12, 22, 25, 64]"

def selection_sort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Input array
arr = [64, 25, 12, 22, 11]

# Perform selection sort
selection_sort(arr)

# Output sorted array
print(arr)  # Output: [11, 12, 22, 25, 64]


# 1. **Implement Stack using Queue**: Use Python's queue data structure to implement a stack.
#     - *Input*: push(1), push(2), pop(), push(3), pop(), pop()
#     - *Output*: "1, None, 3, None, None
from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue = Queue()

    def push(self, item):
        # Get the current size of the queue
        size = self.queue.qsize()

        # Add the new item to the queue
        self.queue.put(item)

        # Rotate the queue to move the new item to the front
        for _ in range(size):
            self.queue.put(self.queue.get())

    def pop(self):
        # If the queue is empty, return None
        if self.queue.empty():
            return None
        
        # Pop the top item from the queue
        return self.queue.get()

# Implementing the given input
stack = StackUsingQueue()
print(stack.pop())  # Output: None
stack.push(1)
stack.push(2)
print(stack.pop())  # Output: 2
stack.push(3)
print(stack.pop())  # Output: 3
print(stack.pop())  # Output: None
print(stack.pop())  # Output: None

# 1. **FizzBuzz**: Write a Python program that prints the numbers from 1 to 100, but for multiples of three, print "Fizz" instead of the number, for multiples of five, print "Buzz", and for multiples of both three and five, print "FizzBuzz".
#     - *Input*: None
#     - *Output*: "1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16,..."



for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz", end=", ")
    elif num % 3 == 0:
        print("Fizz", end=", ")
    elif num % 5 == 0:
        print("Buzz", end=", ")
    else:
        print(num, end=", ")


# 1. **File I/O**: Write a Python program that reads a file, counts the number of words, and writes the count to a new file.
#     - *Input*: A text file named "input.txt" with the content "Hello world"
#     - *Output*: A text file named "output.txt" with the content "Number of words: 2"

        # Read content from input.txt file
with open("input.txt", "r") as file:
    content = file.read()

# Count the number of words in the content
word_count = len(content.split())

# Write the word count to output.txt file
with open("output.txt", "w") as file:
    file.write("Number of words: " + str(word_count))

# 2. **Exception Handling**: Write a Python function that takes two numbers as inputs and returns their division, handling any potential exceptions (like division by zero).
#     - *Input*: 5, 0
#     - *Output*: "Cannot divide by zero."

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Input numbers
num1 = 5
num2 = 0

# Call the function and print the output
output = divide_numbers(num1, num2)
print(output)  # Output: "Cannot divide by zero."


