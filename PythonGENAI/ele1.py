# Your Python program should support the following operations:

# Post Creation: Implement a function that allows the creation of a new post. Each post should have a username and a caption. Use Python data structures (e.g., dictionaries) to represent each post, and store them in a list.

# Post Viewing: Create a function that lists all the posts. This function should return a list of posts, where each
#  post is represented as a dictionary with "username" and "caption" keys.

# Post Deletion: Implement a function that allows the deletion of a post, given its unique ID. You can identify posts by their index in the list. Handle the case when trying to delete a post that does not exist.

# Bonus Tasks:

# Like Feature: Implement a simple "like" feature. Each post should keep track of its likes. Create a function to increase the likes of a post by 1.

# Comment Feature: Implement a simple "comment" feature. Each post should store its comments. Create a function to add a comment to a post.

# Notes:

# You do not need to create a web application or user interface. Focus on creating Python functions that perform the specified actions.Assume that the program will run continuously, so data persistence between runs is not necessary.

# Submission:

# Share your Python solution as a script or a Jupyter Notebook, and provide the code on a platform of your choice (e.g., GitHub).

# This problem statement outlines the basic requirements for creating a Python program that simulates the backend functionality of a Facebook-like application, including posts, likes, and comments.
data=[]

def post_details():
    username=input("enter user username:")
    caption=input("enter user caption:")
    data.append({"username":username,"caption":caption})

def del_details():
    username=input("enter user username:")
    caption=input("enter user caption:")
    data.remove({"username":username,"caption":caption})

n=input("enter 1 post and 2 delete:")
if(n==1):
    post_details()
    print(data)
else:
    del_details()
    print(data)

