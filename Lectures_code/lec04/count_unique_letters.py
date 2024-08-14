# usada para armazenar todos os caracteres que já foram vistos.
counter_string = ""
s = "aaaaaaaaaaaaaaabc"
for char in s:
    if char not in counter_string:
        counter_string += char
print(len(counter_string))
