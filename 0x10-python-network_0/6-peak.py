#!/usr/bin/python3


def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers.

    :param list_of_integers: List of unsorted integers
    :type list_of_integers: list
    :return: Peak element in the list
    :rtype: int
    """

    # Edge cases
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]

    # Initialization
    start_idx = 0
    end_idx = len(list_of_integers) - 1

    # Loop until start_idx < end_idx
    while start_idx < end_idx:
        mid_idx = (start_idx + end_idx) // 2

        # Check if peak is at mid_idx
        if (mid_idx == 0 or list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]) and \
           (mid_idx == len(list_of_integers) - 1 or list_of_integers[mid_idx] > list_of_integers[mid_idx + 1]):
            return list_of_integers[mid_idx]

        # Update search space
        if mid_idx > 0 and list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
            end_idx = mid_idx - 1
        else:
            start_idx = mid_idx + 1

    # If no peak found, return None
    return None
