"""Игра угадай число
Комкомпьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Функция угадывания числа

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    min_number = 1
    max_number = 100
    
    while True:
        
        count += 1
        
        if max_number - min_number > 1:
            predict_number = round(min_number + (max_number - min_number)/2)
            if predict_number < number:
                min_number = predict_number
            elif predict_number > number:
                max_number = predict_number
            else:
                break
            
        elif predict_number > number:
            predict_number -= 1
        elif predict_number < number:
            predict_number += 1
        else: 
            break

    return count


def score_game(random_predict) -> int:
    """Вычисление среднего количества попыток, 
    необходимого для угадывания числа, на 1000 подходов алгоритма

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score

if __name__ == "__main__":
    # RUN
    score_game(random_predict)
