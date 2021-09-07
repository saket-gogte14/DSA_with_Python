##Created by : Saket Gogte
##Purpose : Created a Queues and performs multiple operations on it with the suite of menu itesm on display
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#Class Queue to instantiate a node object
class Queue:
    def __init__(self,value):
        new_node=Node(value)
        self.first=new_node
        self.last=new_node
        self.length=1

    # Func to print the Queue
    def printQueue(self):
        print ("{")
        temp=self.first
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
        print ("}")
    
    #Method to enqueue 
    def enqueue(self,value):
        new_node=Node(value)

        if self.first == None and self.last == None:
            self.first=new_node
            self.last=new_node
        else:
            self.last.next=new_node
            self.last=new_node

        self.length+=1

        return True
    
    #Method to dequeue 
    def dequeue(self):

        if self.length == 0:
            return False
        elif self.first == None and self.last == None:
            self.first=None
            self.last=None
        else:
            temp=self.first
            self.first=temp.next
            temp.next=None
            
        self.length-=1
        return True

def select_first_choices():
    print ("\n\ncreate) Create a Queue \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")

def select_choices():
    print ("\n\nenqueue) Add to the queue \ndequeue) Remove the first element from the Queue \nprint) Print the queue \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")


if __name__ == '__main__':

    my_stack=None

    choice=select_first_choices()
    if choice != "Exit":
        if choice == "create":
            val=input("Enter the value for the initial " + choice + " :")
            my_stack=Queue(val)
    else:
        quit()

    os.system('cls')

    choice=select_choices()
    while choice != "Exit":
        os.system('cls')
        if choice == "enqueue":
            val=input("Enter the value for the initial " + choice + " :")
            my_stack.enqueue(val)
        elif choice == "dequeue":
            my_stack.dequeue()
        elif choice == "print":
            my_stack.printQueue()
        else:
            print ("Invalid Choice....")

        choice=select_choices()
