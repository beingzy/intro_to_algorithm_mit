"""remove the nth node from linked list from the end

   given linked list: 1->2->3->4->5, n = 2

   return: [1, 2, 3, 5]

   author: Yi Zhang <beingzy@gmail.com>
   date: 2018/04/15
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def remove_nth_from_end(head, n):
    """
    """
    probe = head
    behind_n = head
    delay_counter = n
    length = 1

    while probe.next:
        probe = probe.next

        if delay_counter > 0:
            delay_counter -= 1
        else:
            behind_n = behind_n.next

        length += 1

    if length == n:
        head = head.next
        return head

    if n == 1:
        behind_n.next = None
        return head

    behind_n.next = behind_n.next.next
    return head


def traverse_listnode(head):
    cursor = head
    vals = [cursor.val]
    while cursor.next:
        cursor = cursor.next
        vals.append(cursor.val)
    return vals


def test_case_01():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head = remove_nth_from_end(head, 2)
    assert traverse_listnode(head) == [1, 2, 3, 5]


def test_case_02():
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    head = remove_nth_from_end(head, 1)
    assert traverse_listnode(head) == [1, 2, 3, 4]


def test_case_03():
    head = ListNode(1)
    head = remove_nth_from_end(head, 1)
    assert head == None


def test_case_04():
    head = ListNode(1)
    head.next = ListNode(2)
    head = remove_nth_from_end(head, 2)
    assert head == [2]


if __name__ == "__main__":
    test_case_01()
    test_case_02()
    test_case_03()
    test_case_04()
