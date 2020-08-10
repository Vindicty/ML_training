import numpy as np

def game_core_v3(number):
    # Используется метод двоичного поиска на отрезке от 1 до 100

    attepmts = 0
    prediction = 50
    min_possible_guess = 1
    max_possible_guess = 100

    while number != prediction:
        attepmts += 1

        if prediction > number:
            max_possible_guess = prediction - 1
        else:
            min_possible_guess = prediction + 1

        prediction = int((max_possible_guess + min_possible_guess)/2)
    return attepmts


def score_game(game_core):
    # Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число

    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=1000)

    count_ls = [game_core(number) for number in random_array]
    score = round(np.mean(count_ls))

    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

