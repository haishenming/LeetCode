# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
#
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
#
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
#
# 示例：
#
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
#
# Related Topics 链表 数学


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        注意链表的操作技巧
        """
        rdata = ListNode(0)
        curr = rdata

        carry = 0
        while l1 or l2:
            curr.next = ListNode((l1.val if l1 else 0) + (l2.val if l2 else 0) + carry)
            carry = curr.next.val // 10
            curr.next.val %= 10
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry > 0:
            if curr.next:
                curr.next.val += carry
            else:
                curr.next = ListNode(carry)

        return rdata.next


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    s = Solution()
    l11 = ListNode(2)
    l12 = ListNode(4)
    l13 = ListNode(3)

    l11.next = l12
    l12.next = l13

    l21 = ListNode(5)
    l22 = ListNode(6)
    l23 = ListNode(4)

    l21.next = l22
    l22.next = l23

    # l_sum = s.addTwoNumbers(ListNode(0), l21)
    l_sum = s.addTwoNumbers(ListNode(5), ListNode(5))

    while l_sum:
        print(l_sum.val)
        l_sum = l_sum.next
