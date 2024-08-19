def palindrome(s):
    """
    input: s is a string
    output: true if s is palindrome and false otherwise
    """
    invert = s[::-1]
    return s == invert
    
print(palindrome('222'))
print(palindrome('222222'))
print(palindrome('abc'))