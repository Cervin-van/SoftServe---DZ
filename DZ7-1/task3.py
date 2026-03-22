
def counter(word):
    result = {}
    for i in word:
        if i in result:
            result[i] += 1
        else:
            result[i] = 1
    return result

name = input("Введіть ваше ім'я: ")
print(counter(name))