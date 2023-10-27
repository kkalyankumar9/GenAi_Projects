# 1. **Anagram Check**: Write a Python function that checks whether two given words are anagrams.
#     - *Input*: "cinema", "iceman"
#     - *Output*: "True"
word1 = "cinema"
word2 = "iceman"
def anagrams(word1, word2):
    w1=word1.replace(" ","").lower()
    w2=word2.replace(" ","").lower()
    return sorted(w1)==sorted(w2)

print(anagrams(word1, word2))

# 2. **Bubble Sort**: Implement the bubble sort algorithm in Python.
#     - *Input*: [64, 34, 25, 12, 22, 11, 90]
#     - *Output*: "[11, 12, 22, 25, 34, 64, 90]"
arr=[64, 34, 25, 12, 22, 11, 90]
def bubblesort(arr):
    n=len(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]


bubblesort(arr)
print(arr)

# 3. **Longest Common Prefix**: Given a list of strings, find the longest common prefix.
#     - *Input*: ["flower","flow","flight"]
#     - *Output*: "fl"

word= ["flower","flow","flight"]
def comprefix(word):
    prefix=""
    if not word:
        return ""
    word.sort()
    for i in range(len(word[0])):
        if word[0][i]==word[-1][i]:
            prefix+=word[0][i]
        else:
            break
    return prefix


print(comprefix(word))

# 4. **String Permutations**: Write a Python function to calculate all permutations of a given string.
#     - *Input*: "abc"
#     - *Output*: "['abc', 'acb', 'bac', 'bca', 'cab', 'cba']"

from itertools import permutations

def string_permutations(input_string):
    # Generate all permutations of the input string
    perms = permutations(input_string)
    
    # Convert permutations to a list of strings
    result = [''.join(permutation) for permutation in perms]
    
    return result

# Input string
input_string = "abc"

# Get permutations and print the output
permutations_list = string_permutations(input_string)
print(permutations_list)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
