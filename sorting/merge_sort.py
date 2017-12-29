"""
"""


def compare_func(a, b, ascending=True):
    if ascending:
        return a < b
    else:
        return not a < b


def divide_into_sorted_pairs(x, ascending=True):
    """divide x into a list of sorted two-item lists,
    """
    n_items = len(x)
    num_pairs = n_items // 2 if n_items % 2 == 0 else n_items // 2 + 1
    pairs = [None] * num_pairs

    for ii in range(num_pairs):
        a_ii, b_ii = ii * 2, ii * 2 + 1
        if b_ii < n_items:
            a_x, b_x = x[a_ii], x[b_ii]
            pairs[ii] = ([a_x, b_x] if compare_func(a_x, b_x, ascending)
                         else [b_x, a_x])
        else:
            pairs[ii] = [x[a_ii]]

    return pairs


def merge_sorted_list(a_list, b_list, ascending=True):
    """
    """
    tot_a_list, tot_b_list = len(a_list), len(b_list)

    if compare_func(a_list[tot_a_list-1], b_list[0], ascending):
        merged_list = a_list + b_list
    elif compare_func(b_list[tot_b_list-1], a_list[0], ascending):
        merged_list = b_list + a_list
    else:
        merged_list = a_list[:]
        b_inserted_idx = 0
        for key in range(tot_b_list):
            key_val = b_list[key]
            for a_idx in range(b_inserted_idx, len(merged_list)):
                a_val = merged_list[a_idx]
                if compare_func(key_val, a_val, ascending):
                    merged_list.insert(a_idx, key_val)
                    b_inserted_idx = a_idx + 1

    return merged_list


def merge_sort(x, ascending=True):
    """
    """
    raise NotImplementedError
