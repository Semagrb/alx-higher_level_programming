#!/usr/bin/python3

def find_peak(list_of_integers):
    if not list_of_integers or len(list_of_integers) == 0:
        return None

    mid_idx = len(list_of_integers) // 2

    if (mid_idx != len(list_of_integers) - 1 and
            list_of_integers[mid_idx - 1] < list_of_integers[mid_idx] and
            list_of_integers[mid_idx + 1] < list_of_integers[mid_idx]) or \
       (mid_idx == len(list_of_integers) - 1 and
            list_of_integers[mid_idx - 1] < list_of_integers[mid_idx]):
        return list_of_integers[mid_idx]

    if list_of_integers[mid_idx - 1] > list_of_integers[mid_idx]:
        return find_peak(list_of_integers[:mid_idx])
    else:
        return find_peak(list_of_integers[mid_idx + 1:])
