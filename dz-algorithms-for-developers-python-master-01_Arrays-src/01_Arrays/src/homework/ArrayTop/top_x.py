from typing import List


def find_max_under_boundary(input_array: List[int], top_boundary: int) -> int:
    # Найдем текущий максимум
    current_max = float('-inf')

    for item in input_array:
        # Рассмотрим только те элементы, которые меньше заданного числа
        if item < top_boundary:
            current_max = max(current_max, item)

    return current_max


def find_top_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    # Создадим массив для результата
    top_elements = []

    # Нам требуется знать предыдущее значение максимума,
    # По-умолчанию мы положим туда максимальное значение для типа float
    previous_max = float('inf')

    # Выполним цикл столько раз, сколько максимумов нам нужно найти
    for i in range(number_of_elements):
        # Найдем текущий максимум
        current_max = find_max_under_boundary(input_array, previous_max)

        # Обновим значение "предыдущего" максимума
        previous_max = current_max

        # Положим результат в выходной массив
        top_elements.append(current_max)

    return top_elements


def find_bottom_elements(input_array: List[int], number_of_elements: int) -> List[int]:
    # TODO Please implement
    return []


if __name__ == '__main__':
    array = [10, 66, 4, 16, 99, 35, 11, 123]

    top5 = find_top_elements(array, 5)
    print("Top 5:", top5)

    top8 = find_top_elements(array, 8)
    print("Top 8:", top8)
