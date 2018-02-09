def binary_search(item, list):
    low = 0
    high = len(list) - 1
    sorted_list = sorted(list)
    print(sorted_list)

    while low <= high:
        mid = int((low + high)/2)
        guess = sorted_list[mid]

        if guess == item:
            print("Item: ", item, " is on the ", mid, " position in list")
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    print("Item: ", item, " is not on the list")
    return None


if __name__ == '__main__':

    chosen = 2143
    tab = [0, 9, 123, 23, 342, 421, 223, 332, 532, 2143, 523, 234]

    binary_search(chosen, tab)

