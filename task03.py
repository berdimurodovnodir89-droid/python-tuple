words = ("apple", "banana", "strawberry", "kiwi")
max_word = words[0]
for word in words:
    if len(word) > len(max_word):
        max_word = word

print(max_word)