def search(data, item):
    left, right = 0, len(data) - 1

    while left <= right:
        middle = (left + right) // 2

        if item < data[middle]:
            right = middle - 1
        elif item > data[middle]:
            left = middle + 1
        else:
            return middle

    return "not found"
data = [2, 3, 4, 8, 22, 23, 24, 25, 26, 28, 31, 39, 40, 43, 45, 49, 54, 58, 59, 60, 72, 73, 76, 87, 95, 97, 98]
data = sorted(data)
print(search(data, 22))
print(search(data, 4))
print(search(data, 74))
