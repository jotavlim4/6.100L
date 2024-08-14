an_letters = "aefhilmnorsxAEFHILMNORSX"
word = input("I will cheer for you! Type a word: ")
times = int(input("Enthusiam level (1-9): "))

for w in word:
    if w in an_letters:
        print(f'Give me an {w}: {w}!')
    else:
        print(f'Give me a {w}: {w}!')
print("What does that spell?")
for i in range(times):
    print(f"{word}!!!")
