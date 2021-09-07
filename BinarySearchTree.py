##Created by : Saket Gogte
##Purpose : Created a Binary Search Tree and insert and search an element
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#Class BinarySearchTree to instantiate a node object
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while temp is not None:
            if new_node.value == temp.value:
                return False
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    

if __name__ == '__main__':
    my_tree=BinarySearchTree()
    my_tree.insert(40)
    my_tree.insert(80)
    my_tree.insert(30)
    print (my_tree.root.value)
    print (my_tree.root.left.value)
    print (my_tree.root.right.value)
#    print(my_tree.root.left.value)
#    my_tree.insert(50)
#    print(my_tree.root.right.value)