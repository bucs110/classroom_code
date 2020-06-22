

sentence = "In the not-too-distant future, next Sunday A.D."
words = sentence.split()
print(words)
word_lengths = [len(word) for word in words if "-" not in word]

array = [random.uniform(-1, 1) for x in range(10)]
