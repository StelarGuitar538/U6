def merge_sort(arr):
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(arr) <= 1:
        return arr

    # Dividir el arreglo a la mitad
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Conquistar (ordenar ambas mitades recursivamente)
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Combinar ambas mitades ya ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    i = j = 0

    # Combina los elementos de ambas mitades ordenadas
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Agregar los elementos restantes (si los hay) de ambas mitades
    merged.extend(left[i:])
    merged.extend(right[j:])
    
    return merged

# Ejemplo de uso:
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Arreglo ordenado:", sorted_arr)
