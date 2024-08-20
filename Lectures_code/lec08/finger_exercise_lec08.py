def same_chars(s1, s2):
    """
    s1 and s2 are strings
    Returns boolean True is a character in s1 is also in s2, and vice 
    versa. If a character only exists in one of s1 or s2, returns False.
    """
    for char1 in s1:
        flag = True
        if char1 in s2:
            for char2 in s2:
                if char2 in s1:
                   flag = True 
                else:
                    flag = False
        else:
            if char2 in s1:
                flag = False
    return flag

print(same_chars("abc", "cab"))     # prints True
print(same_chars("abccc", "caaab")) # prints True
print(same_chars("abcd", "cabaa"))  # prints False
print(same_chars("abcabc", "cabz")) # prints False