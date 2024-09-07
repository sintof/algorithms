from utils.speed import timeit


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))


@timeit
def depth_first_search(root):
    if not root:
        return
    stack = [root]
    while(len(stack)):
        cur = stack.pop()
        print(cur.val, end=" ")
        if cur.right:
            stack.append(cur.right)
        if cur.left:
            stack.append(cur.left)
    return root


def start():
    depth_first_search(root)