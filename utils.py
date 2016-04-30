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
