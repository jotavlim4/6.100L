def palindrome(s):
    """
    input: s is a string
    output: true if s is palindrome and false otherwise
    """
    return s == s[::-1]
    
print(palindrome('222'))
print(palindrome('222222'))
print(palindrome('abc'))