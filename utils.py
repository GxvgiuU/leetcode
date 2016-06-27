# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function


# for ListNode below
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def print_list(head):
    tmp = head
    print(tmp.val)
    while tmp.next:
        print('->', tmp.val)
        tmp = tmp.next
    print()

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def print_tree(node):
    ''' level order -> http://articles.leetcode.com/how-to-pretty-print-binary-tree/ '''
    def get_info(node):  # return box_size and height
        max_len, h, q, q_ = 0, 0, [node], []
        while q:
            h += 1
            for n in q:
                if n.left:
                    max_len = max(max_len, len(str(n.left.val)))
                    q_.append(n.left)
                if n.right:
                    max_len = max(max_len, len(str(n.right.val)))
                    q_.append(n.right)
            q_, q = [], q_
        return max_len + 1, h
    box_size, height = get_info(node)
    current_level_nodes, next_level_nodes, level = 1, 0, 1
    padding = box_size * (2 ** (height - level) - 1)
    q = [node]
    print('{0:^{width}}'.format('', width=padding / 2), end='')
    while level <= height:
        if (q[0]):
            print('{0:^{width}}'.format(q[0].val, width=box_size), end='')
            q.append(q[0].left)
            q.append(q[0].right)
        else:
            print('{0:^{width}}'.format('', width=box_size), end='')
            q.append(None)
            q.append(None)
        next_level_nodes += 2
        q.pop(0)
        current_level_nodes -= 1
        if not current_level_nodes:
            current_level_nodes, next_level_nodes = next_level_nodes, 0
            level += 1
            padding = box_size * (2 ** (height - level) - 1)
            print('\n{0:^{width}}'.format('', width=max(0, padding / 2)), end='')
        else:
            print('{0:^{width}}'.format('', width=padding), end='')
