##Created by : Saket Gogte
##Purpose : Created a stacks and performs multiple operations on it with the suite of menu itesm on display
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#Class LinkedList to instantiate a node object
class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    # Func to print the list
    def printStack(self):
        print ("{")
        temp=self.top
        if temp:
            for _ in range(self.height-1):
                print(temp.value)
                temp=temp.next
        
        print ("}")
    
    # Func to append to the list    
    def push(self,value):
        new_node=Node(value)

        new_node.next=self.top
        self.top=new_node
        
        self.height=self.height+1

        return True
    
    #Func to remove last node from the list
    def pop(self):

        if self.height == 0:
            return False
        elif self.top.next  == None:
            self.top=None
        else:
            temp=self.top
            self.top=temp.next
            temp.next=None

        self.height=self.height-1
        return True

def select_first_choices():
    print ("\n\ncreate) Create a Stack \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")

def select_choices():
    print ("\n\npush) Append to the list \npop) Pop the top element from the Stack \nprint) Print the stack \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")


if __name__ == '__main__':

    my_stack=None

    choice=select_first_choices()
    if choice != "Exit":
        if choice == "create":
            val=input("Enter the value for the initial " + choice + " :")
            my_stack=Stack(val)
    else:
        quit()

    os.system('cls')

    choice=select_choices()
    while choice != "Exit":
        os.system('cls')
        if choice == "push":
            val=input("Enter the value for the initial " + choice + " :")
            my_stack.push(val)
        elif choice == "pop":
            my_stack.pop()
        elif choice == "print":
            my_stack.printStack()
        else:
            print ("Invalid Choice....")

        choice=select_choices()
