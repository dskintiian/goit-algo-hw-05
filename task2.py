def binary_search(data: list, element, iteration = 0) -> tuple:
    if len(data) == 0:
        return ()

    if len(data) == 1:
        return iteration, data[0]

    mid = len(data) // 2

    if data[mid] > element:
        return binary_search(data[:mid], element, iteration + 1)

    return binary_search(data[mid:], element, iteration + 1)

if __name__ == "__main__":
    print(binary_search([1/3,2/3,3/3,4/3,5/3,6/3,7/3,8/3,9/3], 1))
