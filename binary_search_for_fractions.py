def binary_search(lst, el):
    low = 0
    high = len(lst) - 1
    mid = 0

    iter_counter = 0
    while low <= high:
        iter_counter += 1
        mid = (high + low) // 2

        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if lst[mid] < el:
            low = mid + 1

        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif lst[mid] > el:
            high = mid - 1

        # інакше x присутній на позиції і повертаємо його
        else:
            return iter_counter, lst[mid]

    if low < len(lst):
        return iter_counter, lst[low]
    else:
        return iter_counter, None


arr = [round(i/11, 3) for i in range(10)]
print("Given array: ", arr)
search_val = arr[7]+0.01
print("Searching for: ", search_val)
print(binary_search(arr, search_val))
search_val = arr[7]-0.01
print("Searching for: ", search_val)
print(binary_search(arr, search_val))
search_val = arr[7]
print("Searching for: ", search_val)
print(binary_search(arr, search_val))
