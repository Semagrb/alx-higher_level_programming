def best_score(a_dictionary):
    if a_dictionary:
        max_key = None
        max_value = float('-inf')
        for key, value in a_dictionary.items():
            if value > max_value:
                max_key = key
                max_value = value
        return max_key
    return None

# Test cases
a_dictionary = {'John': 12, 'Bob': 14, 'Mike': 14, 'Molly': 16, 'Adam': 10}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))
