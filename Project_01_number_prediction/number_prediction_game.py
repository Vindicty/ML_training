import numpy as np


def game_core():
    """Predicts number by using Binary Search algorithm"""
    number_to_predict = np.random.randint(1, 101)
    current_prediction = np.random.randint(1, 101)
    prediction_attempts = 0

    min_possible_prediction = 1
    max_possible_prediction = 100

    while True:
        prediction_attempts += 1

        if current_prediction > number_to_predict:
            max_possible_prediction = current_prediction - 1
        elif current_prediction < number_to_predict:
            min_possible_prediction = current_prediction + 1
        else:
            return prediction_attempts

        current_prediction = (min_possible_prediction + max_possible_prediction) // 2


def attempts_statistic(game_core, game_runs=1000):
    """Counts average attemtps amount that need to predict a number"""
    # collect all games results according to specified game rounds
    games_attempts = [game_core() for game_run in range(game_runs)]
    print(
        (
            f'Среднее количество попыток при угадывании числа от 1 до 100 за {game_runs} '
            f'игровых раундов - {round(sum(games_attempts)/len(games_attempts), 2)}'
        )
    )


attempts_statistic(game_core)
