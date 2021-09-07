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

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value == temp.value:
                return True
            elif value < temp.value:
                temp = temp.left
            else:
                temp = temp.right
        
        return False

def select_choices():
    print ("\n\ninsert) Add to the BST \nsearch) Search element from the BST \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")
    

if __name__ == '__main__':
    my_tree=BinarySearchTree()

    choice=select_choices()
    while choice != "Exit":
        os.system('cls')
        if choice == "insert":
            val=input("Enter the value to insert in the Binary Search Tree " + choice + " :")
            my_tree.insert(val)
        elif choice == "search":
            val=input("Enter the value to find in the Binary Search Tree " + choice + " :")
            print(my_tree.contains(val))
        else:
            print ("Invalid Choice....")

        choice=select_choices()

#    print(my_tree.root.left.value)
#    my_tree.insert(50)
#    print(my_tree.root.right.value)