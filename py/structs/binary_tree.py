from utils.speed import timeit


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return "Binary Tree"



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


def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=" ")
        inorder_traversal(root.right)


def preorder_traversal(root):
    if root is not None:
        print(root.val, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)


def postorder_traversal(root):
    if root is not None:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.val, end=" ")


def level_order_traversal(root):
    if root is not None:
        dequeue = [root]
        while dequeue:
            cur = dequeue.pop(0)
            print(cur.val, end=" ")
            if cur.left:
                dequeue.append(cur.left)
            if cur.right:
                dequeue.append(cur.right)


def height(root):
    if root is not None:
        left_height = height(root.left)
        right_height = height(root.right)
        return max(left_height, right_height) + 1
    return 0



def start():
    print(
        """
        Binary Tree Structure
                1
               / \ 
              2   3
             / \ / \ 
            4  5 6  7
        """
    )
    # depth_first_search(root)

    timeit(inorder_traversal)(root)
    timeit(preorder_traversal)(root)
    timeit(postorder_traversal)(root)
    timeit(level_order_traversal)(root)
    print(timeit(height)(root))