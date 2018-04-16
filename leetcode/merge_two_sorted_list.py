"""Merge two sorted linked lists and return it as a new list.
   The new list should be made by splicing together the nodes of the first two lists.

   example:
   * Input: 1->2->4, 1->3->4
   * Output: 1->1->2->3->4->4
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_two_sorted_list(l1, l2):
    """
    """
    if (not l1.next) or (not l2.next):
        return l1 or l2

    if l1.val < l2.val
        l1.next = merge_two_sorted_list(l1.next, l2)
        return l1
    else:
        l2.next = merge_two_sorted_list(l1, l2.next)
        return l2
