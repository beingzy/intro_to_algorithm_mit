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

    def get_left_child(self, idx):
        total_items = len(self._alist)
        left_child_idx = 2 * _from_list_index(idx)
        left_child = self.get_node(_to_list_index(left_child_idx))
        return left_child

    def get_right_child(self, idx):
        right_child_idx = 2 * _from_list_index(idx) + 1
        right_child = self.get_node(_to_list_index(right_child_idx))
        return right_child

    def get_children(self, idx):
        return self.get_left_child(idx), self.get_right_child(idx)


def _to_list_index(i):
    return i - 1


def _from_list_index(i):
    return i + 1


if __name__ == "__main__":
    aheap = Heap([1, 2, 3, 4, 5, 6, 7, 8])
    assert aheap.get_node(0) == 1
    assert aheap.get_node(2) == 3
    assert aheap.get_parent(2) == 1
    assert aheap.get_children(2) == (6, 7)
