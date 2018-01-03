"""Implementation of heap data sctructure,
   heap is an array visualized as complete binary tree
"""

class Heap():

    def __init__(self, alist):
        self._alist = alist

    def get_node(self, idx):
        if idx < len(self._alist):
            return self._alist[idx]
        else:
            return None

    def get_parent(self, idx):
        return self.get_node(_to_list_index(_from_list_index(idx)//2))

    def get_child(self, idx):
        left_child_idx = 2 * _from_list_index(idx)
        right_child_idx = 2 * _from_list_index(idx) + 1
        total_items = len(self._alist)
        left_child = self.get_node(_to_list_index(left_child_idx))
        right_child = self.get_node(_to_list_index(right_child_idx))

        return left_child, right_child


def _to_list_index(i):
    return i - 1


def _from_list_index(i):
    return i + 1
