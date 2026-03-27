from random import randint

secret = randint(1, 100)
attempts = 10

print("Я загадав число від 1 до 100. У тебе є 10 спроб!")

for attempt in range(1, attempts + 1):
    guess = int(input(f"Спроба {attempt}/{attempts}: Введи число: "))

    if guess == secret:
        print(f"Вітаю! Ти вгадав число {secret} за {attempt} спроб(и)!")
        break
    elif guess < secret:
        print("Більше!")
    else:
        print("Менше!")
else:
    print(f"Спроби вичерпано! Загадане число було {secret}.")
