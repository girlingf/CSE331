########################################
# PROJECT 6 - BinarySearchTree
# Author: Frankie Girling
########################################


class Node:
    __slots__ = 'key', 'value', 'parent', 'left', 'right'

    def __init__(self, key, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param key: key associated with the node - package ID in this case
        :param value: value stored at the node - name in this case
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.key = key
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def __eq__(self, other):
        """
        Describes equality comparison for nodes ('==')
        :param other: node being compare to
        :return: True if equal, False if not equal
        """
        if other is None:
            return False
        if self.key == other.key and self.value == other.value:
            return True
        return False
    
    def __repr__(self):
        """
        Defines string representation of a node (str())
        :return: string representing node
        """
        return str(self.key) + ":" + str(self.value)


class BinarySearchTree:

    def __init__(self):
        """
        Initializes an empty Binary Search Tree
        :return nothing
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.size != other.size:
            return False
        if self.root != other.root:
            return False
        if self.root is None or other.root is None:
            return True      # Both must be None

        if self.root.left is not None and other.root.left is not None:
            r1 = self._compare(self.root.left, other.root.left)
        else:
            r1 = (self.root.left == other.root.left)
        if self.root.right is not None and other.root.right is not None:
            r2 = self._compare(self.root.right, other.root.right)
        else:
            r2 = (self.root.right == other.root.right)

        result = r1 and r2
        return result

    def _compare(self, t1, t2):
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if nott
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        result = self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)
        return result

    def inorder(self, node, order_list):
        """
        DO NOT EDIT
        Performs in-order traversal of the BST.
        :param node: root of tree to do in-order traversal (allows for recursive calls)
        :param order_list: running list of BST values (blank list to start)
        :return: list of nodes
        """
        if node is not None:
            self.inorder(node.left, order_list)
            order_list.append(node)
            self.inorder(node.right, order_list)
        return order_list

    def insert(self, key, value):
        """
        If key is not in BST, creates new node. Else, updates value (name) at key.
        :param key: key of new node - determines location of node
        :param value: value of new node
        :return: nothing
        """

        if self.size == 0:
            n1 = Node(key, value)  # new node
            self.root = n1
            self.size += 1

        s = self.search(key, self.root)  # find node

        if key == s.key:
            s.value = value  # replace old node value with new one

        elif key < s.key:  # left side of sub-tree
            s.left = Node(key, value)
            s.left.parent = self.find_parent(key)
            self.size += 1

        else:  # right side of sub-tree
            s.right = Node(key, value)
            s.right.parent = self.find_parent(key)
            self.size += 1

    def remove(self, key):
        """
        Removes a node from BST with given key.
        :param key: key of node to remove
        :return: nothing
        """
        s = self.search(key, self.root)  # current node
        p = self.find_parent(key)  # parent of node

        if s.left and s.right:  # remove node has 2 children

            replace = self.min(s.right)
            s.key = replace.key
            s.value = replace.value

            if replace.left is not None:
                self.max(s.left).right = replace.left

            if replace.right is not None:
                self.min(s.right).left = replace.right

            if replace.parent.left is not None:
                if replace.parent.left.key == s.key:
                    replace.parent.left = None

            elif replace.parent.right is not None:
                if replace.parent.right.key == s.key:
                    replace.parent.right = None

            del replace
            self.size -= 1

        elif s.left or s.right:  # remove node has 1 child

            if s.left:
                replace = s.left
                s.key = replace.key
                s.value = replace.value
                s.left = replace.left
                s.right = replace.right

            else:
                replace = s.right
                s.key = replace.key
                s.value = replace.value
                s.left = replace.left
                s.right = replace.right

            del replace
            self.size -= 1

        elif not s.left and not s.right:  # remove node has no children
            if p.left == s:
                p.left = None

            else:
                p.right = None

            del s
            self.size -= 1

        else:
            pass

    def search(self, key, node):
        """
        Searches the BST for a node with given key.
        :param key: key to search for
        :param node: root of subtree to search for (allows for recursive calls)
        :return: Node with key if found, the nearest leaf node if not found
        """
        if key == node.key:
            return node  # successful search

        elif key < node.key and node.left is not None:  # search left sub-tree
            return self.search(key, node.left)

        elif key > node.key and node.right is not None:  # search right sub-tree
            return self.search(key, node.right)

        else:
            return node  # failed search

    def find_name(self, key):
        """
        Finds the value (name) associated with given key.
        :param key: key associated with the value
        :return: value of the node with the given key, False if not found
        """
        s = self.search(key, self.root)

        if s.key == key:
            return s.value  # node exists

        else:
            return False  # node doesn't exist

    def min(self, node):
        """
        Gets the minimum key of a BST.
        :param node: root of (sub)tree to find minimum
        :return: node with minimum key
        """
        walk = node

        while walk.left is not None:  # min value is the furthest left value
            walk = walk.left

        return walk

    def max(self, node):
        """
        Gets the maximum key of the tree.
        :param node: root of (sub)tree to find maximum
        :return: node with maximum key
        """
        walk = node

        while walk.right is not None:  # max value is the furthest right value
            walk = walk.right

        return walk

    def get_size(self):
        """
        Gets the number of nodes of the BST.
        :return: size of BST
        """
        return self.size

    def find_parent(self, key):
        """
        Finds the parent node of the node's input key
        :param key: key of a node
        :return: the parent node of the node's input key
        """
        parent = None
        current = self.root

        while current is not None and current.key != key:

            parent = current

            if key < current.key:  # go left
                current = current.left

            else:  # go right
                current = current.right

        return parent
