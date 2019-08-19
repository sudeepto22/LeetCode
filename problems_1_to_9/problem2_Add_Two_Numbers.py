# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1: ListNode, l2: ListNode, c=0) -> ListNode:
        """
        Problem 2: Add Two Numbers

        :param l1: ListNode
        :param l2: ListNode
        :param c: int

        :return addition: ListNode
        """
        val = l1.val + l2.val + c
        c = val // 10
        ret = ListNode(val % 10)

        if l1.next is not None or l2.next is not None or c != 0:
            if l1.next is None:
                l1.next = ListNode(0)
            if l2.next is None:
                l2.next = ListNode(0)
            ret.next = self.addTwoNumbers(l1.next, l2.next, c)
        return ret


if __name__ == '__main__':
    list_node1 = ListNode(2)
    list_node1.next = ListNode(4)
    list_node1.next.next = ListNode(3)

    list_node2 = ListNode(5)
    list_node2.next = ListNode(6)
    list_node2.next.next = ListNode(4)

    sum_list_node = Solution().addTwoNumbers(list_node1, list_node2)

    while sum_list_node is not None:
        print(sum_list_node.val)
        sum_list_node = sum_list_node.next
