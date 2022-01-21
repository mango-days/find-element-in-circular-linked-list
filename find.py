# 2 way linked list

class Node :
    def __init__ ( self , data ) :
        self.prev = None
        self.data = data
        self.next = None

class DoubleLinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def insert ( self , data ) :
        if self.head == None :
            self.head = Node ( data )
            self.head.next = self.head
            self.head.prev = self.head
            print ( self.head.prev.data ,"  ", self.head.data ,"  ", self.head.next.data )
            return
        
        temp = self.head
        while temp :
            if temp.next != self.head : temp = temp.next
            else : break
        
        temp.next = Node ( data )
        temp.next.next = self.head
        temp.next.prev = temp
        
        self.head.prev = temp.next
        print ( temp.next.prev.data ,"  ", temp.next.data ,"  ", temp.next.next.data )
        return
    
    def printList ( self ) :
        if self.head == None : return
        
        print ( "pre", "node" , "next" )

        print ( self.head.prev.data ,"  ", self.head.data ,"  ", self.head.next.data )
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            print ( temp.prev.data ,"  ", temp.data ,"  ", temp.next.data )
            temp = temp.next
        return
    
    def find ( self , data ) :
        if self.head == None : return
        
        index = 1
        temp = self.head
        while temp :
            if temp.data == data : return index
            elif temp.next != self.head : temp = temp.next
            else : return None
            index += 1
    

Obj = DoubleLinkedList ()

print ( "inserting nodes ---" )
print ( "pre", "node" , "next" )
for index in range (9) : Obj.insert (index+1)

print ("")
print ( "nodes inserted as ---" )
Obj.printList()

print ("")
print ( "node with data 5 is found at index:" , Obj.find(5) )
print ( "node with data 10 is found at index:" , Obj.find(10) )
print ( "node with data 1 is found at index:" , Obj.find(1) )
print ( "node with data 9 is found at index:" , Obj.find(9) )