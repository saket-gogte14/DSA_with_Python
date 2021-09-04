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
        print ("{", end = '')
        temp=self.head
        if temp != None:
            while temp is not None:
                print(temp.value, end = '')
                if temp != self.tail:
                    print (",", end = '')
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
    
    #Func to remove last node from the list
    def pop(self):
        temp=self.head

        if self.head  == self.tail:
            self.head=None
            self.tail=None
        else:
            while temp.next != self.tail:
                temp=temp.next
            self.tail=temp
            temp.next=None

        self.length=self.length-1


if __name__ == '__main__':
    test_linked_list=LinkedList(4)

    test_linked_list.append(8)
    test_linked_list.append(9)
    
    test_linked_list.printList()

    test_linked_list.pop()
    test_linked_list.append(10)
    test_linked_list.pop()
    test_linked_list.pop()
    test_linked_list.append(11)

    test_linked_list.printList()
