# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # slower than recursive? 中序遍历
        if p and q:
            lp, lq = [p], [q]
            while lp and lq:
                tp, tq = lp.pop(), lq.pop()
                if tp and tq:
                    if tp.val == tq.val:
                        lp.extend([tp.right, tp.left])
                        lq.extend([tq.right, tq.left])
                    else:
                        return False
                elif not tp and not tq:
                    continue
                else:
                    return False
            if lp or lq:
                return False
            else:
                return True
        elif not p and not q:
            return True
        else:
            return False

        # recursive
        if p and q:
            if p.val == q.val:
                return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
            else:
                return False
        elif not p and not q:
            return True
        else:
            return False

a = TreeNode(1)
a.left = TreeNode(2)
a.right = TreeNode(3)
b = TreeNode(1)
b.left = TreeNode(2)
b.left.right = TreeNode(3)
s = Solution()
print s.isSameTree(a, b)
