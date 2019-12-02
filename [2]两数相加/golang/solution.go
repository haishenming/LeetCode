//给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
//
// 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
//
// 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
//
// 示例：
//
// 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
//输出：7 -> 0 -> 8
//原因：342 + 465 = 807
//
// Related Topics 链表 数学

//leetcode submit region begin(Prohibit modification and deletion)
/**
 * Definition for singly-linked list.
 */
package main

import "fmt"

type ListNode struct {
	Val  int
	Next *ListNode
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	l := &ListNode{Val: 0}
	l.Next = &ListNode{Val: 0}

	rl := l.Next
	extr := 0
	for (l1 != nil || l2 != nil) || extr != 0 {
		v1 := 0
		v2 := 0

		if l1 != nil {
			v1 = l1.Val
		}

		if l2 != nil {
			v2 = l2.Val
		}

		val := v1 + v2 + extr
		v := val % 10

		rl.Next = &ListNode{Val: v}

		extr = v / 10

		rl = rl.Next

		if l1 != nil {
			l1 = l1.Next
		}

		if l2 != nil {
			l2 = l2.Next
		}
	}

	return l.Next.Next

}

//leetcode submit region end(Prohibit modification and deletion)

func main() {
	l11 := ListNode{Val: 2}
	l12 := ListNode{Val: 4}
	l13 := ListNode{Val: 3}

	l11.Next = &l12
	l12.Next = &l13

	l21 := ListNode{Val: 5}
	l22 := ListNode{Val: 6}
	l23 := ListNode{Val: 4}

	l21.Next = &l22
	l22.Next = &l23

	l := addTwoNumbers(&l11, &l21)

	for l != nil {
		fmt.Println(l.Val)
		l = l.Next
	}

}
