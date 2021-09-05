##Created by : Saket Gogte
##Purpose : Created a doublt linked list and performs multiple operations on it with the suite of menu items on display
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None

#Class DoublyLinkedList to instantiate a node object
class DoublyLinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    # Func to print the list
    def printList(self):
        print ("{", end = '')
        temp=self.head
        if temp != None:
            while temp is not None:
                print(temp.value, end = '')
                if temp != self.tail:
                    print ("<->", end = '')
                temp=temp.next
        
        print ("}")
    
    # Func to append to the list    
    def append(self,value):
        new_node=Node(value)

        if self.head == None and self.tail == None:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            new_node.prev=self.tail
            self.tail=new_node
        
        self.length=self.length+1

        return True
    
    #Func to remove last node from the list
    def pop(self):

        if self.length == 0:
            return False
        elif self.head  == self.tail:
            self.head=None
            self.tail=None
        else:
            temp=self.tail.prev
            self.tail.prev=None
            self.tail=temp
            temp.next=None

        self.length=self.length-1
        return True

    def prepend(self,value):
        new_node=Node(value)

        if self.head == None and self.tail == None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node
        
        self.length=self.length+1

        return True

    def pop_first(self):

        if self.length == 0:
            return False
        elif self.head  == self.tail:
            self.head=None
            self.tail=None
        else:
            first_on_list=self.head
            self.head=first_on_list.next
            self.head.prev=None
            first_on_list.next=None

        self.length=self.length-1

        return True
    
    def get(self,index):
        if self.length == 0 or index < 0 or index > self.length-1:
            return None

        if index < self.length/2:
            temp = self.head
            for _ in range(index):
                temp=temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev

        return temp
    
    def set_value(self,index,value):            
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.prepend(value)
        elif index == self.length:
            return self.append(value)
        else:
            temp=self.get(index)
            new_node=Node(value)
            temp.prev.next=new_node
            new_node.prev=temp.prev
            temp.prev=new_node
            new_node.next=temp
            self.length+=1
            return True
    
    def remove(self,index):

        if index < 0 or index > self.length:
            return False
        elif index == 0:
            return self.pop_first()
        elif index == self.length-1:
            return self.pop()
        else:
            temp=self.get(index)
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.prev=None
            temp.next=None
            return True
        
def select_first_choices():
    print ("\n\ncreate) Create a linked list \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")

def select_choices():
    print ("\n\nappend) Append to the list \nprepend) Prepend to the list \npop) Pop the last element from the list \npop_first) Pop the first element from the list \nget) Get value at a particular index \nset) Set value at a particular index \ninsert) Insert value at a particular index \nremove) Remove value from a particular index position \nprint) Print the Doubly linked list \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")


if __name__ == '__main__':

    doubly_linked_list=None

    choice=select_first_choices()
    if choice != "Exit":
        if choice == "create":
            val=input("Enter the value for the initial " + choice + " :")
            doubly_linked_list=DoublyLinkedList(val)
    else:
        quit()

    os.system('cls')

    choice=select_choices()
    while choice != "Exit":
        os.system('cls')
        if choice == "append":
            val=input("Enter the value to " + choice + " :")
            doubly_linked_list.append(val)
        elif choice == "prepend":
            val=input("Enter the value to " + choice + " :")
            doubly_linked_list.prepend(val)
        elif choice == "insert":
            val=input("Enter the value to " + choice + " :")
            index=input("Enter the index to " + choice + "  :")
            doubly_linked_list.insert(int(index),val)
        elif choice == "pop":
            doubly_linked_list.pop()
        elif choice == "pop_first":
            doubly_linked_list.pop_first()
        elif choice == "set":
            val=input("Enter the value to " + choice + " :")
            index=input("Enter the index to " + choice + "  :")
            doubly_linked_list.set_value(int(index),val)
        elif choice == "get":
            index=input("Enter the index to " + choice + "  :")
            print(doubly_linked_list.get(int(index)).value)
        elif choice == "remove":
            index=input("Enter the index to " + choice + "  :")
            doubly_linked_list.remove(int(index))
        elif choice == "print":
            doubly_linked_list.printList()
        else:
            print ("Invalid Choice....")

        choice=select_choices()
