def find_last(s, sub):
    """
        * s and sub are non-empty strings
        * returns the index of the last occurrence of sub in s.
        * returns None if sub does not occur in s
    """
    if s.find(sub) == -1:
        return None
    i = last_occurence = s.find(sub)
    while i != -1:
        invert = s[i: i + len(sub)]
        s = s[0:i] + invert[::-1] + s[i + len(sub):]
        last_occurence = i
        i = s.find(sub)
    return last_occurence
           
answer = find_last('joa é legal, joa é chato', 'joa') #should return 18
print(answer)


