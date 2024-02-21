#This program takes input from a user and prints out the alternate characters in lowercase

word = input("Please enter a sentence: ")

word_length = len(word)

word_new = []

#Every other letter in a word is basically counting in 2's like even numbers
#So i used a for-loop to change any character occupying an even number position to an upper case character.

for i in range(word_length):
    if i % 2 == 0:
        word_new.append(word[i].upper())

    else:
        word_new.append(word[i].lower())

print('-'*len("".join(word_new)))
print("".join(word_new))
print('-'*len("".join(word_new)))


#Program converts alternate words to uppercase and lowercase
sentence = input("Please enter a sentence: ")

#Because we want the words and not characters, we split the sentence first and treat each word like a single character.

new_sentence1 = sentence.split()
new_sentence_length = len(new_sentence1)
new_sentence2 = []

for i in range(new_sentence_length):
    if i % 2 == 0:
        new_sentence2.append(new_sentence1[i].upper())

    else:
        new_sentence2.append(new_sentence1[i].lower())


#We then rejoin the words after the conversion is finished.

print('-'*len("".join(new_sentence2)))
print(" ".join(new_sentence2))
print('-'*len("".join(new_sentence2)))