#!/usr/bin/python3


def find_peak(list_of_integers):

    if not list_of_integers:
        return None

    mid_idx = len(list_of_integers) // 2

    if mid_idx > 0 and mid_idx < len(list_of_integers) - 1:
        if list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] > list_of_integers[mid_idx + 1]:
            return list_of_integers[mid_idx]

    if mid_idx == 0 or list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]:
        a_list = list_of_integers[mid_idx + 1:]
    else:
        a_list = list_of_integers[:mid_idx]

    return find_peak(a_list)
