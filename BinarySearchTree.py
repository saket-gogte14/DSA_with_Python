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
    
    def BFS(self):
        current_node = self.root
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)

            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
        
        return results
    
    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)
        
        traverse(self.root)

        return results

    def dfs_post_order(self):
        results = []

        def traverse(current_node):                
            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

            results.append(current_node.value)
        
        traverse(self.root)

        return results

    def dfs_in_order(self):
        results = []

        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            results.append(current_node.value) 
            if current_node.right is not None:
                traverse(current_node.right)

        
        traverse(self.root)

        return results    

def select_choices():
    print ("\n\ninsert) Add to the BST \nsearch) Search element from the BST \nBFS) Perform a BFS on the BST \nDFSPreorder) Perform a DFS PreOrder on the BST \nDFSPostorder) Perform a DFS PostOrder on the BST \nDFSInorder) Perform a DFS InOrder on the BST \nExit) Exit the menu")
    
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
        elif choice == "BFS":
            print(my_tree.BFS())
        elif choice == "DFSPreorder":
            print(my_tree.dfs_pre_order())
        elif choice == "DFSPostorder":
            print(my_tree.dfs_post_order())
        elif choice == "DFSInorder":
            print(my_tree.dfs_in_order())
        else:
            print ("Invalid Choice....")

        choice=select_choices()