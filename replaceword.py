
sentence_1 = str(input("Enter a sentence: "))

old_word = str(input("What word would you want to change?: "))

new_word = str(input(f"What word would you want to replace {old_word} with?: "))

sentence_1 = sentence_1.replace(old_word, new_word)

print(f"Your new sentence is: \n {sentence_1}")
