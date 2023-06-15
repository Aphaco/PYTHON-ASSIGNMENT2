sentence = input("Enter a sentence: ")
new_sentence = ""
i = 0
while i < len(sentence):
    char = sentence[i]
    if char in "aeiouAEIOU":
        i += 1
        continue 
    new_sentence += char
    i += 1
print("Modified sentence:", new_sentence)