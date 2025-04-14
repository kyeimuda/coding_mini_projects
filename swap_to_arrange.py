#!/usr/bin/python3

def swap_to_arrange(list1):
    list_len = len(list1)

    while True:
        swapped = False
        for idx in range(list_len):
            if idx != (list_len - 1):
                if list1[idx] > list1[idx + 1]:
                    temp = list1[idx]
                    list1[idx] = list1[idx + 1]
                    list1[idx + 1] = temp
                    swapped = True

        if not swapped:
            break

    print(list1)
