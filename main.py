import time
import random

# Функції сортування та їх асимптотичні складності
sorting_algorithms = {
    "Сортування вибором": ("O(N^2)   ", lambda arr: selection_sort(arr)),
    "Сортування вставками": ("O(N^2)  ", lambda arr: insertion_sort(arr)),
    "Сортування бульбашкою": ("O(N^2) ", lambda arr: bubble_sort(arr)),
    "Сортування злиттям": ("O(N log N)", lambda arr: merge_sort(arr)),
    "Вбудоване сортування": ("O(N log N)", lambda arr: python_builtin_sort(arr))
}


# Функція для сортування методом вибору (Selection Sort)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# Функція для сортування методом вставки (Insertion Sort)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


# Функція для сортування методом обміну (Bubble Sort)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Функція для сортування методом злиття (Merge Sort)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1


# Функція для виклику вбудованого методу сортування Python
def python_builtin_sort(arr):
    arr.sort()


# Функція для вимірювання часу сортування
def measure_sorting_time(sort_function, arr):
    start_time = time.time()
    sort_function(arr)
    end_time = time.time()
    return end_time - start_time


# Функція для генерації випадкового масиву заданої довжини
def generate_random_array(size):
    return [random.randint(1, 1000) for _ in range(size)]

print("Методи сортування написано студентом групи КС-23-2/11 Кирилов Владиславом")

# Виведення заголовку таблиці
print("=" * 137)
print("| {:<19} | {:<22} | {:<20} | {:<14} | {:<14} | {:<15} | {:<11} |".format("Кількість елементів", "Алгоритм сортування",
                                                                             "Асимптотичний склад", "І дослідження", "ІІ дослідження", "ІІІ дослідження", "Середнє"))
print("=" * 137)

# Розміри масивів для тестування
array_sizes = [1000, 10000, 50000]

# Тестування для кожного розміру масиву
for size in array_sizes:
    array = generate_random_array(size)

    # Виведення рядка таблиці для кожного алгоритму
    for algorithm, (complexity, sort_func) in sorting_algorithms.items():
        timings = []

        # Проведення досліджень та вимірювання часу
        for _ in range(3):
            arr_copy = array.copy()
            time_taken = measure_sorting_time(sort_func, arr_copy)
            timings.append(time_taken)

        # Виведення результатів у формі таблиці
        avg_time = sum(timings) / len(timings)
        print("| {:<19} | {:<22} | {:<20} | {:<14f} | {:<14f} | {:<15f} | {:<11f} |".format(size, algorithm, complexity, timings[0],
                                                                            timings[1], timings[2], avg_time))
