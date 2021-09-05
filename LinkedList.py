##Created by : Saket Gogte
##Purpose : Created a linked list 
import os
#Class Node to instantiate a node object
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

#Class LinkedList to instantiate a node object
class LinkedList:
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
                    print ("->", end = '')
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
            temp=self.head
            while temp.next != self.tail:
                temp=temp.next
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
            first_on_list.next=None

        self.length=self.length-1

        return True
    
    def get(self,index):
        if self.length == 0 or index < 0 or index > self.length-1:
            return None

        temp = self.head
        for _ in range(index):
            temp=temp.next
        
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
            temp=self.get(index-1)
            new_node=Node(value)
            new_node.next=temp.next
            temp.next=new_node
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
            pre=self.get(index-1)
            post=self.get(index+1)
            pre.next.next=None
            pre.next=post
            return True
        
    def reverse(self):
        temp=self.head
        after=self.head.next
        before=None
        temp_head=self.head
        self.head=self.tail
        self.tail=temp_head

        while temp != None:
            temp.next=before
            before=temp
            temp=after
            if after != None:
                after=after.next

def select_first_choices():
    print ("\n\ncreate) Create a linked list \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")

def select_choices():
    print ("\n\nappend) Append to the list \nprepend) Prepend to the list \ninsert) Pop the last element from the list \npop_first) Pop the first element from the list \nget) Get value at a particular index \nset_value) Set value at a particular index \ninsert) Insert value at a particular index \nremove) Remove value from a particular index position \nreverse) Reverse the linked list \nprint) Print the linked list \nExit) Exit the menu")
    
    return input("\nEnter the choices from the above display:")


if __name__ == '__main__':

    linked_list=None

    choice=select_first_choices()
    if choice != "Exit":
        if choice == "create":
            val=input("Enter the value for the initial " + choice + " :")
            linked_list=LinkedList(val)
    else:
        quit()

    os.system('cls')

    choice=select_choices()
    while choice != "Exit":
        os.system('cls')
        if choice == "create":
            val=input("Enter the value for the initial " + choice + " :")
            linked_list=LinkedList(val)
        elif choice == "append":
            val=input("Enter the value to " + choice + " :")
            linked_list.append(val)
        elif choice == "prepend":
            val=input("Enter the value to " + choice + " :")
            linked_list.prepend(val)
        elif choice == "insert":
            val=input("Enter the value to " + choice + " :")
            index=input("Enter the index to " + choice + "  :")
            linked_list.insert(int(index),val)
        elif choice == "pop":
            linked_list.pop()
        elif choice == "pop_first":
            linked_list.pop_first()
        elif choice == "set":
            val=input("Enter the value to " + choice + " :")
            index=input("Enter the index to " + choice + "  :")
            linked_list.set_value(int(index),val)
        elif choice == "get":
            index=input("Enter the index to " + choice + "  :")
            print(linked_list.get(int(index)).value)
        elif choice == "remove":
            index=input("Enter the index to " + choice + "  :")
            linked_list.remove(int(index))
        elif choice == "reverse":
            linked_list.reverse()
        elif choice == "print":
            linked_list.printList()
        else:
            print ("Invalid Choice....")

        choice=select_choices()
