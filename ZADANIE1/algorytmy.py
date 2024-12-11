#Marcin Słonka
from ZADANIE1.tablica import MonitorowanaTablica

def insertion_sort(array: MonitorowanaTablica, left=0, right=None):
    if right is None:
        right = len(array) - 1

    i = left + 1
    while i <= right:
        j = i
        while j > left and array[j - 1] > array[j]:
            array[j - 1], array[j] = array[j], array[j - 1]
            j -= 1
        i += 1


def bubble_sort(array: MonitorowanaTablica):
    n = len(array)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

                swapped = True

        if not swapped:
            break


def shell_sort(array: MonitorowanaTablica):
    left = 0
    right = len(array) - 1

    h = 1
    while h <= (right - left) // 9:
        h = 3 * h + 1

    while h > 0:
        for i in range(left + h, right + 1):
            j = i

            item = array[i]
            while j >= left + h and item < array[j - h]:
                array[j] = array[j - h]
                j = j - h
            array[j] = item

        h = h // 3



def merge_sort(array: MonitorowanaTablica, left=None, right=None):
    if left == None:
        left = 0
    if right == None:
        right = len(array)-1

    if left == right:
        return

    m = (left+right)//2

    #rekurencyjne wywołanie merge sort dla 2 kawałków, nic nie zwraca bo operuje na array
    merge_sort(array,left,m)
    merge_sort(array,m+1,right)
    
    #scalenie fragmentow
    merge(array, left, m, right)

def merge(array: MonitorowanaTablica, left, middle, right):
    
    bound1 = middle+1
    bound2 = right+1
    p1 = left
    p2 = middle+1

    bufor = []
    while p1 < bound1 or p2 < bound2:
        if p1 == bound1:
            bufor.append(array[p2])
            p2 += 1
        elif p2 == bound2:
            bufor.append(array[p1])
            p1 += 1
        elif array[p1] <= array[p2]:
            bufor.append(array[p1])
            p1 += 1
        else:
            bufor.append(array[p2])
            p2 += 1

    #przepisanie posortowanego z bufora do array
    for i, elem in enumerate(bufor, left):
        array[i] = elem


def quick_sort(array: MonitorowanaTablica, left=None, right=None):
    """Performs quick sort on the given array."""
    if left == None:
        left = 0
    if right == None:
        right = len(array)-1
        
    i = left
    j = right
    p = (i+j)//2

    while i <= j:
        if (array[i] <= array[p]):
            i += 1
        elif (array[j] >= array[p]):
            j -= 1
        else:
            #zamiana liczb miejscami tak aby byly po dobrej stronie pivota
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    #zmiana pivota tak aby rozdzielał wartości od siebie mniejsze od wartości od siebie większych
    if p < j:
        array[p], array[j] = array[j], array[p]
        p = j
    elif p > i:
        array[p], array[i] = array[i], array[p]
        p = i


    #rekurencyjne wywołanie
    if left < p-1:
        quick_sort(array, left, p-1)

    if p+1 < right:
        quick_sort(array, p+1, right)


def partition(array: MonitorowanaTablica, left, right):
    """Partitions the array into two parts."""
    # twoj kod, moze sie przydac
    pass


def tim_sort(array: MonitorowanaTablica):
    #ustalenie minrun
    n = len(array)
    minrun = get_min_run(array)
    #print(minrun)

    i = 0
    while i < n:
        right = min(i+minrun-1,n-1) #gdy nie da sie rowno podzielic, to ostatnia grupa ma tyle elementów ile zostało
        insertion_sort(array, i, right)
        i += minrun

    #łączenie (parami)
    run_size = minrun
    while run_size < n:
        p = 0
        while p < n:
            m = p + run_size - 1
            q = min(m + run_size, n - 1)

            if m < q:
                merge(array, p, m, q) #łączenie

            p += 2 * run_size #łączę parami
            
        run_size *= 2 #łączę coraz większe grupy


def get_min_run(array: MonitorowanaTablica):
    n = len(array)

    #obliczam ile liczb od początku jest już poukładanych, algorytm ten powinien dobrze radzić sobie z danymi wstępnie poukładanymi, 
    #czy też grupami poukłdanych danych w całej sekwencji (takie często są rzeczywiste dane)
    i = 1
    while i < n and array[i-1] < array[i]:
        i += 1

    #jeśli dane te nie są wstępnie poukładane, czyli jeśli liczba rosnących od początku elementów jest większa lub równa 8
    # to zwracam długość tablicy, jeśli nie to obliczam minrun w sposób standardowy
    if i >= 8:
        return i;
    else:

    # # standardowe (według wikipedii) obliczanie minrun dla timsort:
    # # standardowo bierze się 6 najbardziej znaczących bitów z liczby elementów w tablicy
    # # przesuwa się je na początek, jeśli którykolwiek inny bit był inny niż zero, to dodaje się 1
    # # to powoduje że minrun jest brany z zakresu 32 do 63 włącznie, 
    # # jeśli rozmiar tablicy jest mniejszy niż 64, to tablica ta nie jest dzielona grupy
    # # w tym wypadku, aby zaprezentować działanie algorytmu w pełni, zamiast 6 bitów biorę 4
    # # dla n=50 dostajemy 13

        r = 0
        while n >= 16: # standardowo n >= 64
            r |= n & 1 # detekcja czy którykolwiek z pozostałych bitów jest zapalone
            n >>= 1 # przesuwanie na początek
        return n + r



algorytmy = [
    # (insertion_sort, "Insertion Sort"),
    # (bubble_sort, "Bubble Sort"),
    # (shell_sort, "Shell Sort"),
    # (merge_sort, "Merge Sort"),
    (quick_sort, "Quick Sort"),
    (tim_sort, "Tim Sort"),
]