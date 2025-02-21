"""1. Ordenamientos Simples
Son fáciles de implementar, pero menos eficientes para grandes conjuntos de datos.

a) Bubble Sort (Ordenamiento Burbuja)
Descripción: Compara elementos adyacentes y los intercambia si están en el orden incorrecto.
Complejidad:

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
b) Selection Sort (Ordenamiento por Selección)
Descripción: Encuentra el elemento más pequeño y lo coloca en la primera posición, repitiendo el proceso para el resto de la lista.
Complejidad: 

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
c) Insertion Sort (Ordenamiento por Inserción)
Descripción: Inserta cada elemento en su posición correcta en una sublista ya ordenada.
Complejidad:

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
2. Ordenamientos Eficientes
Estos son más rápidos para listas grandes.

a) Merge Sort (Ordenamiento por Mezcla)
Descripción: Divide la lista en mitades, las ordena recursivamente y luego las combina.
Complejidad: 

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
b) Quick Sort (Ordenamiento Rápido)
Descripción: Selecciona un "pivote" y reorganiza la lista para que los elementos menores estén a la izquierda y los mayores a la derecha. Se aplica recursivamente.
Complejidad:
 
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
c) Heap Sort (Ordenamiento por Montículo)
Descripción: Convierte la lista en un montículo (heap) y extrae el elemento más grande repetidamente.
Complejidad: 

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l

    if r < n and arr[r] > arr[largest]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
3. Ordenamientos Especiales
Counting Sort: Ordena números en un rango limitado (𝑂(𝑛+𝑘)
Radix Sort: Ordena números por sus dígitos (𝑂(𝑛𝑘)
Bucket Sort: Divide los elementos en "cubetas" y los ordena O(n+k)).
"""