"""
Assume you are given a string variable named my_str.
Write a piece of Python code that prints out a new string containing the even indexed characters of my_str.
For example, if my_str = "abcdefg" then your code should print out aceg.
"""

my_str = "0123456789"
only_even_index = ""
for i in range(len(my_str)):
    if i % 2 == 0:
        only_even_index += my_str[i]
print(f"{only_even_index}")
