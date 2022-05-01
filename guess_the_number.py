
import random

EASY_LIFES_GAME = 10
HARD_LIFES_GAME = 5

def chek_answer(random_number,new_user_number,lifes):
    if random_number == new_user_number:
        print ("Ты угадал !")
        print (random_number)
    elif random_number > new_user_number:
        print("Нет, число больше твоего. Попробуй ещё!")
        return lifes - 1
    elif random_number < new_user_number:
        print("Нет, число меньше твоего. Попробуй ещё! ")
        return lifes - 1


def level_choise():
    game_level = input("Выбери уровень игры: Легко or Трудно: ").lower()
    if game_level == 'легко':
        return EASY_LIFES_GAME
    else:
        return HARD_LIFES_GAME


def game():
    random_number = random.randint(1,100)
    print("Привет! Я загадал цифру от 1 до 100. Угадай какую!")
    print(random_number)
    lifes = level_choise()
    new_user_number = 0
    while new_user_number != random_number:
        print(f"У тебя осталось {lifes} жизней")
        new_user_number = int(input("Угадай число от 0 до 100: "))
        lifes = chek_answer(random_number,new_user_number,lifes)
        if lifes == 0:
            print("Жизни закончились! Конец игры!")
            return

game()





