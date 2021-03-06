import random

DRAGON = 0
SWORD = 1
APPLE = 2
# Соотношение появление событий в пропорции DRAGON:SWORD:APPLE
PROBABILITY_EVENT = [7, 2, 2]
# monster_counter - счетчик поверженных героем чудовищ,
# hp - текущее состояние здоровье героя,
# attack - текущая сила удара героя
monster_counter = 0
hp = 10
attack = 10


def get_rnd_event():
    """Генерирует случайное событие в игре"""
    global DRAGON, SWORD, APPLE, PROBABILITY_EVENT
    return random.choices([DRAGON, SWORD, APPLE], weights=PROBABILITY_EVENT)[0]


def read_choice(message: str) -> bool:
    """Печать вопроса и чтение на него ответа, возвращает True в случае согласия, False в противном случае"""
    i = 0
    print(message)
    while not (i == 1 or i == 2):
        i = int(input("Ввести 1 - если ДА, 2 - если НЕТ : "))
    return i == 1


def dragon_event():
    """ Логика для события Встреча c чудовищем """
    global hp, attack, monster_counter
    # Генерация случайного чудовища
    dragon_hp = random.randrange(1, 15)
    dragon_attack = random.randrange(1, 10)
    if read_choice(
            "Встреча с чудовищем [жизни "
            + str(dragon_hp)
            + ", сила удара "
            + str(dragon_attack)
            + "], вступить в БОЙ ?"
    ):
        # чудовище отнимает у рыцаря число жизней, соответствующее его атаке
        hp -= dragon_attack
        if hp > 0 and attack > dragon_hp:
            # число его атаки должно превосходит число жизней чудовища.
            monster_counter += 1
            print("Вы победили чудовище, количество ваших жизней " + str(hp))
        else:
            # если сила атаки чудовища превосходит (или равна) количество жизней рыцаря — рыцарь умирает
            hp = 0
    else:
        print("Вы спаслись от чудовища, продолжаем игру")


def sword_event():
    """ Логика для события Встреча нового меча """
    global attack
    new_sword = random.randrange(6, 16)

    if read_choice(
            "Появился мечь, сила удара " + str(new_sword) + " Взять новый мечь ?"
    ):
        attack = new_sword
        print("Новая сила удара " + str(attack))
    else:
        print("Продолжаем игру со старым мечом")


def apple_event():
    """ Логика для события Яблко """
    global hp
    apple_hp = random.randrange(1, 5)
    hp += apple_hp
    print(
        "Рыцарь съел яблоко, + "
        + str(apple_hp)
        + " жизни, "
        + "теперь у вас "
        + str(hp)
        + " жизней"
    )


def game():
    """ Логика игры """
    global hp, monster_counter
    while hp > 0 and monster_counter < 10:
        game_event = get_rnd_event()
        if game_event == DRAGON:
            dragon_event()
        elif game_event == SWORD:
            sword_event()
        else:
            apple_event()
    print(("ПОРАЖЕНИЕ В ИГРЕ...", "ПОБЕДА !!!")[hp > 0])


# вызов игры
game()
