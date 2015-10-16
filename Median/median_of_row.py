__author__ = 'Dandelion'

import re


def merge(list1, list2):
    """
    Merge procedure from merge sort algorithm.

    :param list list1: First list to merge. It should be sorted in some order.
    :param list list2: Second list to merge. It should be sorted in the same order as first one.
    :return: Sorted list of elements both from 1st and 2nd parameters.

    Merge procedure is needed for merging two sorted in the same order lists of elements in one sorted list.
    Sorting order of result list is similar to both parameters' ones.
    """
    res = [None] * (len(list1) + len(list2))
    i = j = k = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            res[k] = list1[i]
            i += 1
        else:
            res[k] = list2[j]
            j += 1
        k += 1
    while i < len(list1):
        res[k] = list1[i]
        i += 1
        k += 1
    while j < len(list2):
            res[k] = list2[j]
            j += 1
            k += 1
    return res


def median(row1, row2):
    """
    Find median for row with elements from both parameters.

    :param list row1: First row of values. Must be sorted in some way.
    :param list row2: Second row of values. Must be sorted in some way.
    :return: Median of row of values.

    For joining both rows of values :py:func:`merge()` is used
    """
    if (row1[0] <= row1[-1] and row2[0] <= row2[-1] or row1[0] >= row1[-1] and row2[0] >= row2[-1]):
        row = merge(row1, row2)
    else:
        # merge needs sorted in the SAME order lists
        row = merge(row1, row2.reverse())
    print "Row is :", " ".join(map(str, row))
    if len(row) % 2:
        return row[len(row) / 2]
    else:
        return float(row[len(row) / 2 - 1] + row[len(row) / 2]) / 2


def row_input(num):
    """
    Input row of floats from console.

    :param int num: Number of row that needs to be input.
    :return: List of floats extracted from input string.

    List values should be input in one string. `row_input()` allows multiple spaces. In case of any error while
    extracting floats from input string error message is shown and `row_input()` welcomes to try input again.
    Input is retried until it is successful.
    """
    while (1):
        row_str = re.sub(r' +', ' ', raw_input("Input row " + str(num) +  ": ").strip())
        try:
            return map(float, row_str.split(' '))
        except ValueError as err:
            print "Invalid input data:", err.message


def main():
    """
    Main function that inputs two rows of floats and finds median of joined row.

    :return: Nothing is returned.

    `main()` prints joined row and it's median in console. For finding median :py:func:`median()` is used.
    """
    row1 = row_input(1)
    row2 = row_input(2)
    res = median(row1, row2)
    print "Median is", res


if __name__ == "__main__":
    main()
