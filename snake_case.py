word = str(input())
camel_word = ""

for char in word:
    if char.isupper():
        char = char.replace(char, "_"+char.lower())
        camel_word+=char
    else:
        camel_word+=char
print(camel_word)