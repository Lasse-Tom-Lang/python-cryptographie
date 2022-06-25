from random import randint
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890?!,.\ "

result = []
file = open("NumbersForKeys.csv", "w")
file.write("Key;Number\n")
for letter in letters:
    a = randint(100, 1000)
    while a in result or a + 1 in result or a - 1 in result or a + 2 in result or a - 2 in result:
        a = randint(100, 1000)
    result.append(a)
    file.write(f"{letter};{str(a)}\n")

file.close()
