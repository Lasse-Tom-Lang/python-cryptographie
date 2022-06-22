from random import randint
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!,.\ "

result = []
print("Key;Number")
for letter in letters:
    a = randint(100, 1000)
    while a in result or a + 1 in result or a - 1 in result or a + 2 in result or a - 2 in result:
        a = randint(100, 1000)
    result.append(a)
    print(letter + ";" + str(a))
