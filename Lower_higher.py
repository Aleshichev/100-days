import random
from game_data import data
from art_lower import logo, vs

def random_data():
    players = random.choice(data)
    return players

def format_data(players):
    """Берёт данные и возвращает отформатированные данные"""
    account_name = players["name"]
    account_discr = players["description"]
    account_country = players["country"]
    return f"{account_name}, {account_discr}, {account_country} "

def check_answer(who, a_follower_count, b_follower_count ):
    """Берёт значение who и возвращает если оно правильно"""
    if a_follower_count > b_follower_count:
        return who == "а"   # если who != а то False
    else:
        return who == "б"  # если who != б то False

print(logo)
count_try = 0
game_should_continue = True
players_b = random_data()

while game_should_continue:
    players_a = players_b     # приравниваем б к а
    players_b = random_data()     # выбираем ещё один б
    if players_a == players_b:   # если случайно а = б то б выбрать ещё раз
        players_b = random.choice(data)
    print(f"Участник А: {format_data(players_a)}")
    print(vs)
    print(f"Против участника Б: {format_data(players_b)}")
    who = input("Кто имеет больше поклонников? Игрок 'А' или угрок 'Б'? : ").lower()
    a_follower_count = players_a['follower_count']
    b_follower_count = players_b['follower_count']

    is_correct = check_answer(who, a_follower_count, b_follower_count )
    if is_correct:
        count_try += 1
        print(f"Ты угадал {count_try} раз")
    else:
        game_should_continue = False
        print(f"Нееет.Ты угадал {count_try} раз")


