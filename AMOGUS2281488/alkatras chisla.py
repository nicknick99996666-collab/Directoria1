import random

secret_number = random.randint(1, 100)
attempts = 0

while True:
    user_input = input("Угадай число от 1 до 100 или сдайся(GG)")

    if user_input == "GG":
        print("Ты сдался. Число было:")
        print(secret_number)
        break

    number = int(user_input)
    attempts = attempts + 1

    if number < secret_number:
        print("слишком маленькое")
    elif number > secret_number:
        print("слишком большое")
    else:
        print("ты угадал число")
        print("Попыток:")
        print(attempts)
        break