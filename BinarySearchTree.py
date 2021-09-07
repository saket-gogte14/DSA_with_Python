##Created by : Saket Gogte
##Purpose : Created a Binary Search Tree and insert and search an element
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

#Class BinarySearchTree to instantiate a node object
class BinarySearchTree:
    def __init__(self):
        self.rootptr = None
    
    def insert(self,value):
        new_node=Node(value)
        if self.rootptr is None:
            self.rootptr=new_node
            return True

        temp = self.rootptr
        
        while (True):
            
            if int(value) < int(temp.value):
                print(self.rootptr)
                if temp.left is not None:
                    temp.left = new_node
                    return True
                temp = temp.left
            elif value > int(temp.value):
                if temp.right is not None:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif value == int(temp.value):
                return False

    

if __name__ == '__main__':
    my_tree=BinarySearchTree()
    print(my_tree.insert(40))
    
    print(my_tree.insert(80))
#    print(my_tree.rootptr.left.value)
#    my_tree.insert(50)
#    print(my_tree.rootptr.right.value)