# -*- coding: utf-8 -*-
from __future__ import unicode_literals


# for ListNode below
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
def print_list(head):
    tmp = head
    while tmp:
        print tmp.val, '->',
        tmp = tmp.next
    print

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
def print_tree(node):
    ''' level order '''
    q = [node]
    while filter(None, q):
        q_ = []
        for n in q:
            if not n:
                print '\u2205',
            else:
                print n.val,
                q_.append(n.left)
                q_.append(n.right)
        q = q_
        print
