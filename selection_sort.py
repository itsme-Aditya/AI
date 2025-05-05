def selection_sort(arr):
    print("Original array: ", data)
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    print("Array after selection sort: ", data)

def enter_data():
    n  = int(input("Enter number of elements to add in array: "))
    for i in range(0, n):
        elem = int(input(f"Enter element {i + 1}: "))
        data.append(elem)

data = []
enter_data()
selection_sort(data)
