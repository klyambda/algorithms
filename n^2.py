"""Сложность данных алгоритмов сортировки O(n^2)"""


def bubble_sort(array):
    """Алгоритм пузырьковой сортировки.

    Популярный, но не эффективный алгоритм сортировки. В его основе лежит многократная
    перестановка соседних элементов, нарушающих порядок сортировки.
    """
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def insertion_sort(array):
    """Алгоритм сортировки вставками.

    Данный алгоритм эффективно работает при сортировке небольшого кол-ва элементов,
    не использует дополнительную память.
    """

    # в начале каждой итерации массив разделен на две части:
    # первая часть отсортированная, вторая неотсортированная
    for j in range(1, len(array)):
        # индекс j указывает на текущий элемент
        key = array[j]
        # индекс i указывает на элемент из отсортированной части
        i = j - 1

        # помещаем key в отсортированную часть
        while i >= 0 and array[i] > key:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = key

    return array


def selection_sort(array):
    """Алгоритм сортировки выбором.

    Находит самый маленький элемент из неотсортированной части массива
    и помещает его в конец отсортированной части.
    """
    for i in range(len(array)):
        min_idx = i
        for j in range(i, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]

    return array
