"""a number is stored as linked list (e.g. (3 -> 4 -> 5) = 543), task is
   to compute the sum of two number stored by a pair of linked list. The
   result of the sum should be stored as linked list as well.
"""
class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


def convert_to_number(linked_list):
    step = 0
    num = linked_list.val
    next_item = linked_list.next
    while next_item:
        step += 1
        num += next_item.val * (10**step)
        next_item = next_item.next
    return num


def convert_to_linkedlist(num):
    digits = list(str(num))
    val = int(digits.pop())
    repr_list = ListNode(val)
    current = repr_list
    while digits:
        val = int(digits.pop())
        current.next = ListNode(val)
        current = current.next
    return repr_list


def add_two_numbers(alist, blist):
    ans = convert_to_number(alist) + convert_to_number(blist)
    return convert_to_linkedlist(ans)


if __name__ == "__main__":
    a_list = ListNode(3)
    a_list.next = ListNode(4)
    a_list.next.next = ListNode(5)
    assert convert_to_number(a_list) == 543

    b_list = convert_to_linkedlist(712)
    assert b_list.val == 2
    assert b_list.next.val == 1
    assert b_list.next.next.val == 7

    # input (2 -> 4 -> 3) + (5 -> 6 -> 4)
    # Output: 7 -> 0 -> 8
    alist = ListNode(2)
    alist.next = ListNode(4)
    alist.next.next = ListNode(3)

    blist = ListNode(5)
    blist.next = ListNode(6)
    blist.next.next = ListNode(4)

    ans_list = ListNode(7)
    ans_list.next = ListNode(0)
    ans_list.next.next = ListNode(8)

    ans = add_two_numbers(alist, blist)
    print(ans.next.next.val * 100 + ans.next.val * 10 + ans.val)
