input = input("Please enter.")
words = input.split()
for i, word in enumerate(words):
    if word == ':)':
        words[i] = '🙂'
    if word == ':(':
        words[i] = '🙁'
        
for word in words:
    print(word, end = " ")
print("\n")