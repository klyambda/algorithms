from random import randint

def quick_sort(array, p, r):
    """Алгоритм быстрой сортировки

    Разделение: Массив A[p..r] разделяется на два подмассива A[p..q-1] и A[q+1..r],
    элемент A[q] не меньше любого элемента из второго подмассива и не больше любого
    элемента из первого. Индекс q вычисляется в ходе процедуры разбиения.
    Властвование: Подмассивы A[p..q-1] и A[q+1..r] сортируются с помощью рекурсивного
    вызова процедуры быстрой сортировки.
    Комбинирование: Поскольку подмассивы сортируются на месте, для их объединения не
    требуется никакие действия: весь массив A[p..r] оказывается отсортированным.
    Наихудшее время работы быстрой сортировки O(n^2). Несмотря на это, данный алгоритм
    на практике является оптимальный благодаря тому, что в среднем время его работы O(nlgn).
    Кроме того, постоянный множитель, скрытый в выражении O(nlgn), достаточно мал по величине.
    Не использует дополнительную память. Время работы алгоритма зависит от степени сбалансиро-
    ванности, которой характеризуется разбиение. Сбалансированность зависит от того, какой
    элемент выбран в качестве опорного. Наихудший случай - в качестве опорного элемента
    выбран максимальный (или минимальный) элемент.
    """
    if p < r:
        q = randomized_partition(array, p, r)
        quick_sort(array, p, q - 1)
        quick_sort(array, q + 1, r)


def partition(array, p, r):
    """Разбиение массива

    Изменяет порядок элеметов подмассива A[p..r], не используя дополнительную память.
    В первой части массива содержатся элементы, меньшие опорного элемента, во второй
    - большие. В качестве опорного элемента берем конец подмассива A[p..r].
    Время работы процедуры partition над подмассивом A[p..r] равно O(n), n = r - p + 1
    """
    pivot = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] <= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    # опорный элемент помещается на свое место в середину массива с помощью
    # его перестановки с крайним левым элементом, превышающим его
    array[i + 1], array[r] = array[r], array[i + 1]
    # возвращает новый индекс опорного элемента
    return i + 1


def randomized_partition(array, p, r):
    """Разбиение массива со случайной выборкой

    Случайный выбор опорного элемента обеспечивает равную вероятность любому из
    r - p + 1 элементов оказаться опорным. Благодаря случайному выбору опорного
    элемента можно ожидать, что разбиение входного массива в среднем окажется
    довольно хорошо сбалансированным.
    """
    rand = randint(p, r)
    array[rand], array[r] = array[r], array[rand]
    return partition(array, p, r)