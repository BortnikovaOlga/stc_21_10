import random
import sys

DRAGON = 0
SWORD = 1
APPLE = 2
# Соотношение появление событий в пропорции DRAGON:SWORD:APPLE
PROBABILITY_EVENT = [7, 2, 7]
# monster_counter - счетчик поверженных героем чудовищ,
# hp - текущее состояние здоровье героя,
# attack - текущая сила удара героя
monster_counter = 0
hp = 10
attack = 10


def get_rnd_event() -> int:
    """Генерирует случайное событие в игре."""
    global DRAGON, SWORD, APPLE, PROBABILITY_EVENT
    return random.choices([DRAGON, SWORD, APPLE], weights=PROBABILITY_EVENT)[0]


def read_choice(message: str) -> bool:
    """Печать вопроса и чтение на него ответа, возвращает True в случае согласия, False в противном случае."""
    i = ""
    while not (i == "1" or i == "2"):
        print(message)
        i = input("Ввести 1 - если ДА, 2 - если НЕТ : ").strip()
    return i == "1"


def dragon_event() -> None:
    """Логика для события Встреча c чудовищем."""
    global hp, attack, monster_counter
    # Генерация случайного чудовища
    dragon_hp = random.randrange(1, 4)  # 15 было для реальной игры
    dragon_attack = random.randrange(1, 4)  # 10 было для реальной игры
    if read_choice(
            "БОЙ с чудовищем жизни "
            + str(dragon_hp)
            + " сила удара "
            + str(dragon_attack)
            + " вступить в БОЙ ?"
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


def sword_event() -> None:
    """Логика для события Встреча нового меча."""
    global attack
    new_sword = random.randrange(6, 16)

    if read_choice("МЕЧ сила удара " + str(new_sword) + " Взять новый меч ?"):
        attack = new_sword
        print("Новая сила удара " + str(attack))
    else:
        print("Продолжаем игру со старым мечом")


def apple_event() -> None:
    """Логика для события Яблоко."""
    global hp
    apple_hp = random.randrange(1, 10)
    hp += apple_hp
    print("ЯБЛОКО + " + str(apple_hp) + " теперь у вас " + str(hp) + " жизней")


def game() -> None:
    """Логика игры."""
    global hp, monster_counter
    print(
        "Игра Рыцарь и чудовища, цель игры - победить 10 чудовищ\n"
        + "в ходе игры можно менять меч,\n"
        + "чудовище возможно победить только при условии, когда у меча сила удара больше, чем жизней у чудовища,\n"
        + "а количество жизней у рыцаря больше чем сила чудовища\n"
        + "Рыцарь вступает в игру с 10 жизнями и мечом с ударом 10\n"
    )
    while hp > 0 and monster_counter < 10:
        game_event = get_rnd_event()
        if game_event == DRAGON:
            dragon_event()
        elif game_event == SWORD:
            sword_event()
        else:
            apple_event()
    print(
        "ПОБЕДА Вы победили " + str(monster_counter) + " чудовищ"
        if hp > 0
        else "ПОРАЖЕНИЕ В ИГРЕ..."
    )
    sys.exit(1)


# вызов игры
if __name__ == "__main__":
    game()
