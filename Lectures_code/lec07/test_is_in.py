def is_in(s1: str, s2: str):
    return s1 in s2

def test_is_in(strings1: tuple, strings2: tuple):
    
    for s1 in strings1:
        for s2 in strings2:
            result = is_in(s1, s2)
            if result:
                val = 'Okay'
            else:
                val = 'Do not in'
            print(f"{s1} in {s2}? {val}")
    
str1 = ('joao', 'joa', 'jo', 'j', 'victor', 'victo', 'vict', 'vic', 'vi', 'v')
str2 = ('joao', 'victor', 'joao victor')

test_is_in(str1, str2)