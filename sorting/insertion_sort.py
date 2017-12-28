"""
"""

def insertion_sort(x, ascending=True):
    """sort x in ascending order.
    """
    def compare_func(a, b, ascending=ascending):
        if ascending:
            return a > b
        else:
            return not a > b

    sorted_x = x[:]
    key = 1 # 0 index-based
    x_len = len(sorted_x)
    for key in list(range(1, x_len)):
        left_to_key = key - 1
        left_val, key_val = sorted_x[left_to_key], sorted_x[key]

        while compare_func(left_val, key_val):
            sorted_x[left_to_key], sorted_x[key] = key_val, left_val
            left_to_key, key = left_to_key - 1, key - 1

            if left_to_key < 0:
                break
            else:
                left_val, key_val = sorted_x[left_to_key], sorted_x[key]

    return sorted_x
