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
        elif index == self.length:
            return self.pop()
        else:
            pre=self.get(index-1)
            post=self.get(index+1)
            pre.next.next=None
            pre.next=post
            return True

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
    test_linked_list.prepend(14)
    test_linked_list.printList()
    test_linked_list.pop_first()
    test_linked_list.printList()
    #print(test_linked_list.get(1).value)
    test_linked_list.set_value(0,20)
    test_linked_list.printList()
    test_linked_list.insert(2,40)
    test_linked_list.printList()
    test_linked_list.remove(2)
    test_linked_list.printList()
    