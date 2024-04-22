# array

lista = [32, 12, 54, 21, 5, 42, 17, 61, 30, 49, 11, 9, 25, 38, 57, 3, 48, 14, 46, 27, 50, 59, 36, 20, 1, 7, 63, 55, 28, 44, 16, 33, 53, 10, 58, 31, 22, 4, 19, 41, 60, 24, 34, 8, 43, 18, 52, 2, 39, 56, 45, 6, 23, 26, 62, 29, 51, 37, 15, 64, 47, 35]

def bubble_short(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_short(lista))
