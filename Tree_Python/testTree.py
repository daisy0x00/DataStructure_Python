#coding:utf-8

import queue

# 建立二叉树结点
class TreeNode():
    def __init__(self, elem = None, left = None, right = None):
        self.elem = elem
        self.left = left
        self.right = right


class Tree():
    # 初始化二叉树
    def __init__(self, root = None):
        self.root = root

    
# 递归遍历二叉树
    # 递归前序遍历二叉树
    def pre_order_recursion(self, root):
        if root == None:
            return
        print(root.elem)
        self.pre_order_recursion(root.left)
        self.pre_order_recursion(root.right)

    # 递归前序遍历二叉树
    def in_order_recursion(self, root):
        if root == None:
            return
        self.in_order_recursion(root.left)
        print(root.elem)
        self.in_order_recursion(root.right)

    # 递归前序遍历二叉树
    def post_order_recursion(self, root):
        if root == None:
            return
        self.post_order_recursion(root.left)
        self.post_order_recursion(root.right)
        print(root.elem)

# 非递归遍历二叉树
    def post_order_without_recursion(self, root):
        stack_node = queue.LifoQueue()



if __name__ == '__main__':
    # 创建二叉树
    root = TreeNode('D', TreeNode('B', TreeNode('A'), TreeNode('C')), TreeNode('E', right = TreeNode('G', TreeNode('F'))))
    tree = Tree()

    print('pre_order_recursion: ')
    tree.pre_order_recursion(root)
    print('\n')

    print('in_order_recursion: ')
    tree.in_order_recursion(root)
    print('\n')

    print('post_order_recursion: ')
    tree.post_order_recursion(root)
    print('\n')