import string
from nltk import word_tokenize

f = open('Dogs_heart_Bulgakov.txt', "r", encoding="utf-8")
text = f.read()

spec_chars = '\n\xa0«»\t—…!"#$%&"()*+,-./:;<=>?@[\]^_`{|}~0123456789'



text = text.lower()
text = "".join([ch for ch in text if ch not in spec_chars])
word = text.split()

print(word[:300])

print("Количество слов:", len(word), "\nКоличество символов:", len(text))