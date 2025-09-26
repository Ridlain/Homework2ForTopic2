word = input("word = ")
word_len = len(word)
if word_len % 2 != 0:
    print("Результат:",word[word_len//2])
else:
    print("Результат:",word[(word_len//2)-1:(word_len//2)+1])