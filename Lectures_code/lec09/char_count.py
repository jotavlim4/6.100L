def char_counts(s):
    """
        s is a string of lowercase chars
        returns a tuple were the first elements is 
        the number of vowel in s and the second is the 
        number of consoants in s
    """
    vowels = 'aeiou'
    count_vowels, count_consoants = 0, 0
    for v in s:
        if v in vowels:
            count_vowels += 1
        else:
            if v != ' ':
                count_consoants += 1
    return count_vowels, count_consoants
    
vowels, consoants = char_counts('Joao victor liam da silva')
answer = char_counts('Joao victor liam da silva')
print(vowels, consoants)
print(answer[0], answer[1])