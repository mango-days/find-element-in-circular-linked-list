# find an element in a circularly linked list

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class CircularLinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def insert ( self , data ) :
        if self.head == None :
            self.head = Node ( data )
            self.head.next = self.head
            return
        
        # find last element
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            prev = temp
            if temp.next != None : temp = temp.next
            
        # insert element
        prev.next = Node ( data )
        prev.next.next = flag
        return
    
    def printList ( self ) :
        if self.head == None :
            print ( "List empty" )
            return
        
        temp = self.head.next
        prev = self.head
        flag = self.head
        while temp != flag :
            print ( temp.data )
            temp = temp.next
        return
    
    def find ( self , data ) :
        if self.head == None :
            print ( "Not found" )
            return
        
        temp = self.head.next
        found = False
        flag = self.head
        count = 0
        
        while temp != flag:
            count += 1
            if temp.data == data :
                found = True
                break
            temp = temp.next
            
        if found == True : print ( "Found at :" , count )
        else : print ( "Not found" )
        
        return
            
CllObj = CircularLinkedList ()

for index in range ( 10 ) : 
    CllObj.insert ( index )
    
CllObj.find (11)
CllObj.find (6)
CllObj.find (2)
CllObj.find (0)
