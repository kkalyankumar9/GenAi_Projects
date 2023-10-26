

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
