class SingleList:  
    
    def __init__(self,data):
        self.data= data
        self.next= None       
    
    
class LinkedList:
    def __init__(self):
        self.head=None        
                       
    def __repr__(self) -> str:
        cur_node=self.head
        while cur_node:
            print(cur_node.data)
            cur_node=cur_node.next
     
    def append_item(self,value): 
        firstnode=SingleList(data=value)    
        if self.head is None:
            firstnode=SingleList(data=value)     
            self.head=firstnode
            return           
       
        lastnode=self.head
        while lastnode.next:
                lastnode=lastnode.next
        lastnode.next=firstnode
    def remove(self):
        
        if self.head is not None:
            temp=self.head.data
            self.head=self.head.next
            
            return self.head
        
item1=LinkedList()
item1.append_item('5')
item1.append_item('8')
print(item1.__repr__())
print(item1.remove())


