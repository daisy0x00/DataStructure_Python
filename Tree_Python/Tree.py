#coding:utf-8

import queue
# 二叉树的节点表示
class TreeNode():
    """
    二叉树节点
    """
    def __init__(self, elem = 1, left = None, right = None):
        self.elem = elem
        self.left = left
        self.right = right

# Part I树的创建
# 创建一个树的类，并给一个root根节点，一开始为空，随后添加节点
class Tree():
    """
    二叉树
    """
    def __init__(self, root = None):
        self.root = root

    def add(self, elem):
        """
        为树添加节点
        :param elem:
        :return:
        """
        node = TreeNode(elem)
        # 如果树是空的，则对根节点赋值
        if self.root == None:
            self.root = node
        else:
            queue = list()
            queue.append(self.root)
            while queue:
                # 弹出队列的第一个元素
                cur = queue.pop(0)
                if cur.left == None:
                    cur.left = node
                    return
                elif cur.right == None:
                    cur.right = node
                    return
                else:
                    # 如果左右子树都不为空，往判断列表加入子树，循环进行子树的判断
                    queue.append(cur.left)
                    queue.append(cur.right)

# Part II 二叉树的遍历
# 递归实现深度优先遍历
    # 递归先序遍历：根节点->左子树->右子树
    def pre_order_recursion(self, root):
        """
        递归实现先序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        print(root.elem)
        self.pre_order_recursion(root.left)
        self.pre_order_recursion(root.right)

    # 递归中序遍历：左子树->根节点->右子树
    def in_order_recursion(self, root):
        """
        递归实现中序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        self.in_order_recursion(root.left)
        print(root.elem)
        self.in_order_recursion(root.right)

    # 递归后序遍历：左子树->右子树->根节点
    def post_order_recursion(self, root):
        """
        递归实现后序遍历
        :param root:
        :return:
        """
        if root == None:
            return
        self.post_order_recursion(root.left)
        self.post_order_recursion(root.right)
        print(root.elem)
# 非递归实现深度优先遍历

    # 非递归先序遍历：根节点->左子树->右子树
    def pre_order_without_recursion(self, root):
        """
        非递归先序遍历
        使用栈保存结点信息
        :param root:
        :return:
        """
        # 栈
        stack_node = queue.LifoQueue()
        while(root is not None or not stack_node.empty()):
            if root is not None:
                print(root)
                stack_node.put(root.right)
                root = root.right
            else:
               root = stack_node.get()


    # 非递归中序遍历：左子树->根节点->右子树
    def in_order_without_recursion(self, root):
        """
        非递归中序遍历
        使用栈保存结点信息
        :param root:
        :return:
        """
        stack_node = queue.LifoQueue()
        while(root is not None or not stack_node.empty()):
            if root is not None:
                stack_node.put(root)
                root = root.left
            else:
                root = stack_node.get()
                print(root)
                root = root.right
    # 非递归后序遍历：左子树->右子树->根节点
    tags = {'left': 'Left', 'right': 'Right'}
    def post_order_without_recursion(self, root):
        """
        非递归后序遍历
        使用栈保存结点信息
        对父节点已访问过的左右子树做标记
        :param root:
        :return:
        """
        stack_node = queue.LifoQueue()
        while(root is not None or not stack_node.empty()):
            while(root is not None):
                root.tag = self.tags['left']
                stack_node.put(root)
                root = root.left
            root = stack_node.get()
            if(root.tag == self.tags['left']):
                root.tag = self.tags['right']
                stack_node.put(root)
                root = root.right
            else:
                print(root)
                root = None
    def post_order_without_recursion_1(self, root):
        """
        非递归后序遍历
        使用栈保存结点信息
        保存前一个被访问过的结点
        :param root:
        :return:
        """
        stack_node = queue.LifoQueue()
        pre = root
        while(root is not None):
            while(root.left is not None):
                stack_node.put(root)
                root = root.left
            # 当前结点没有右孩子或者右孩子刚被访问过，则访问该结点
            while(root is not None and (root.right is None or root.right == pre)):
                print(root)
                pre = root
                if(stack_node.empty()):
                    return
                root = stack_node.get()
            stack_node.put(root)
            root = root.right


# 广度优先遍历（层次遍历）
    def breadth_travel(self, root):
        """
        利用队列的先进先出规则实现树的层次遍历
        :param root:
        :return:
        """

        if root == None:
            return
        # queue队列，保存结点
        queue = list()
        # res保存结点值，作为结果
        queue.append(root)

        while queue:
            # 拿出队首结点
            current_node = queue.pop(0)
            print(current_node.elem)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)

if __name__=='__main__':
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    f = TreeNode(6)
    g = TreeNode(7)
    a.left = b
    a.right = c
    b.right = d
    c.left = e
    c.right = f
    f.left = g
    test = Tree()
    print("levelOrder:",end=' ')
    test.breadth_travel(a)
    print("\nRecursionPreOrder:",end=' ')
    test.pre_order_recursion(a)
    print("\nRecursionInOrder:",end=' ')
    test.in_order_recursion(a)
    print("\nRecursionPostOrder:",end=' ')
    test.post_order_recursion(a)
    print("\nPreOrderWithoutRecursion:",end=' ')
    test.pre_order_without_recursion(a)
    print("\nInOrderWithoutRecursion:",end=' ')
    test.in_order_without_recursion(a)
    print("\nPostOrderWithoutRecursion:",end=' ')
    test.post_order_without_recursion(a)
    print("\nPostOrderWithoutRecursion_1:",end=' ')

