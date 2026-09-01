"""
Structure of comments:
Function description.
Time complexity O()
"""

class BSTNode:
    def __init__(self, key):
        self.left = self.right = self.parent = None
        self.key = key
        self.value = None

    def __repr__(self):
        return f"({self.key}, {self.value})"


class BinarySearchTree:
    # Initialize an empty Binary Search Tree.
    # Time complexity O(1)
    def __init__(self): self.root = None

    # Return the number of nodes in the tree.
    # Time complexity O(n)
    def __len__(self): return len(list(self._in_order_traversal(self.root)))
    
    # Check if a key exists in the tree using the 'in' operator.
    # Time complexity O(log n) average, O(n) worst case
    def __contains__(self, item):
        curr_node = self.root

        while curr_node is not None:
            if item < curr_node.key: curr_node = curr_node.left
            elif item > curr_node.key: curr_node = curr_node.right
            else: return True
        return False

    # Iterate through tree nodes in in-order traversal.
    # Time complexity O(n)
    def __iter__(self): yield from self._in_order_traversal(self.root)

    # Return string representation of tree as a sorted list.
    # Time complexity O(n)
    def __repr__(self): return str(list(self._in_order_traversal(self.root)))

    # Insert a key-value pair into the tree maintaining BST property.
    # Time complexity O(log n) average, O(n) worst case
    def insert(self, key, value):
        new_node = BSTNode(key)

        if self.root is None:
            self.root = new_node
            self.root.value = value

        else:
            curr_node = self.root
            while True:
                if key < curr_node.key:
                    if curr_node.left is None:
                        curr_node.left = new_node
                        curr_node.left.value = value
                        curr_node.left.parent = curr_node
                        break

                    else: curr_node = curr_node.left

                elif key > curr_node.key:
                    if curr_node.right is None:
                        curr_node.right = new_node
                        curr_node.right.value = value
                        curr_node.right.parent = curr_node
                        break

                    else: curr_node = curr_node.right

                else: 
                    curr_node.value = value
                    break

    # Search for a node by key and return it or None.
    # Time complexity O(log n) average, O(n) worst case
    def search(self, key):
        curr_node = self.root

        while True:
            if curr_node is None or curr_node.key == key: return curr_node

            elif key < curr_node.key:
                if curr_node.left is None: return None
                else: curr_node = curr_node.left

            else:
                if curr_node.right is None: return None
                else: curr_node = curr_node.right

    # Delete a node by key handling three cases: leaf, one child, two children.
    # Time complexity O(log n) average, O(n) worst case
    def delete(self, key):
        node = self.search(key)

        if node is None: raise ValueError("Node with this key does not exist!")

        self._delete(node)

    # Traverse tree in specified order: 'inorder', 'preorder', or 'postorder'.
    # Time complexity O(n)
    def traverse(self, order):
        if order.lower() == "inorder": yield from self._in_order_traversal(self.root)
        elif order.lower() == "preorder": yield from self._pre_order_traversal(self.root)
        elif order.lower() == "postorder": yield from self._post_order_traversal(self.root)
        else: raise ValueError("Unkown input!")

    # Internal method to delete a node with proper tree restructuring.
    # Time complexity O(log n) average, O(n) worst case
    def _delete(self, node):
        if node.left is None and node.right is None:
            if node.parent is None: self.root = None
            else:
                if node.parent.right  == node: node.parent.right = None
                else: node.parent.left = None
                node.parent = None

        elif node.left is None or node.right is None:
            child_node = node.left if node.left is not None else node.right

            if node.parent is None:
                child_node.parent = None
                self.root = child_node
            
            else:
                if node.parent.right == node: node.parent.right = child_node
                else: node.parent.left = child_node
                child_node.parent = node.parent
            node.parent = node.left = node.right = None

        else:
            successor = self._successor(node)

            node.key = successor.key
            node.value = successor.value

            self._delete(successor)

    # Find the in-order successor (leftmost node in right subtree).
    # Time complexity O(log n) average, O(n) worst case
    def _successor(self, node):
        if node is None: raise ValueError("Cannot find successor of None!")

        if node.right is None: return None
        else: 
            curr_node = node.right

            while curr_node.left is not None: curr_node = curr_node.left
            return curr_node

    # Find the in-order predecessor (rightmost node in left subtree).
    # Time complexity O(log n) average, O(n) worst case
    def _predecessor(self, node):
        if node is None: raise ValueError("Cannot find predecessor of None!")
        
        if node.left is None: return None
        else: 
            curr_node = node.left

            while curr_node.right is not None: curr_node = curr_node.right
            return curr_node

    # Perform in-order traversal (Left, Root, Right) yielding (key, value) pairs.
    # Time complexity O(n)
    def _in_order_traversal(self, node):
        if node is not None:
            yield from self._in_order_traversal(node.left)
            yield (node.key, node.value)
            yield from self._in_order_traversal(node.right)

    # Perform post-order traversal (Left, Right, Root) yielding (key, value) pairs.
    # Time complexity O(n)
    def _post_order_traversal(self, node):
        if node is not None:
            yield from self._post_order_traversal(node.left)
            yield from self._post_order_traversal(node.right)
            yield (node.key, node.value)

    # Perform pre-order traversal (Root, Left, Right) yielding (key, value) pairs.
    # Time complexity O(n)
    def _pre_order_traversal(self, node):
        if node is not None:
            yield (node.key, node.value)
            yield from self._pre_order_traversal(node.left)
            yield from self._pre_order_traversal(node.right)

    # Check if the tree is empty.
    # Time complexity O(1)
    def is_empty(self): return self.root == None


if __name__ == "__main__":
    print("==" * 30, "\nBinary Search Tree:\nBeginning:\n", "__" * 30)
    print()

    BST = BinarySearchTree()

    BST.insert(10, "Ismail")
    BST.insert(5, "hamada")
    BST.insert(22, "sam")
    BST.insert(12, "mo")
    BST.insert(2, "salah")
    BST.insert(9, "abdo")
    BST.insert(12, "sara")
    BST.insert(30, "isra'a")
    BST.insert(11, "widad")
    BST.insert(15, "ishaq")
    BST.insert(30, "ishaq")
    BST.insert(23, "ishaq")
    BST.insert(35, "ishaq")

    print(len(BST))
    print(BST)
    print(35 in BST)
    print(BST.search(30))

    BST.delete(23)

    print(BST.traverse("postordeR"))

    for k in BST: print(k)
    for k in BST.traverse("preorder"): print(k)


    