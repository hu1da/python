# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если в слово длинное, выводить только первые 10 букв в слове.

sentence = input("enter a sentence: ")
words = sentence.split()
length = len(words)
current = 0
while current < length:
    print(words[current][:10])
    current += 1
