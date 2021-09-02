##Created by : Saket Gogte
##Purpose : Created a linked list 

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
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
    
    # Func to append to the list    
    def append(self,value):
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        
        new_node=Node(value)
        temp.next=new_node
        self.tail=new_node
        self.length=self.length+1

test_linked_list=LinkedList(4)

test_linked_list.append(8)
test_linked_list.append(9)

test_linked_list.printList()

print(test_linked_list.length)
