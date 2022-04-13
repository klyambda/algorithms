"""Алгоритмы поиска"""


def linear_search(array, item):
    """Линейный поиск"""

    for i in range(len(array)):
        if array[i] == item:
            return i
    return -1
    

def binary_search(array, item):
    """Бинарный поиск"""

    left = 0
    right = len(array) - 1
    
    while left < right:
        mid = (left + right) // 2
        if  array[mid] < item:
            left = mid + 1
        elif array[mid] > item:
            right = mid - 1
        else:
            return mid
    return -1
