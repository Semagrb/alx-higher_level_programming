#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """Delete an item at a specific position in a list."""
    if idx < 0 or idx >= len(my_list):
        return my_list  # Index out of range, no change to the list
    
    del my_list[idx]
    return my_list

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    idx_to_delete = 2
    result = delete_at(my_list, idx_to_delete)
    print(result) 
