class last:
    def __init__(self,last=None):
        self.last=last

    def isempty(self):
        return self.last==None
    
    def insert_at_start(self,data):
        n=node(data)
        if self.isempty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n

    def insert_at_last(self,data):
        n=node(data)
        if self.isempty():
            n.next=n
            self.last=n
        else:
            n.next=self.last.next
            self.last.next=n
            self.last=n

    def search(self,data):
        if self.isempty():
            return None
        temp=self.last.next
        while temp!=self.last:
            if temp.item==data:
                return temp
            temp=temp.next
        if temp.item==data:
            return temp
        return None
        
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next)
            temp.next=n
            if temp==self.last:
                self.last=n

    def print_list(self):
        if not self.isempty():
            temp=self.last.next
            while temp!=self.last:
                print(temp.item,end=' ')
                temp=temp.next
            print(temp.item) 

    def delete_first(self):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else:
                self.last.next=self.last.next.next

    def delete_last(self):
        if not self.isempty():
            if self.last.next==self.last:
                self.last=None
            else:
                temp=self.last.next
                while temp.next!=self.last:
                    temp=temp.next
                temp.next=self.last.next
                self.last=temp

    def delete_after(self,data):
        if not self.isempty():
            if self.last.next==self.last:
                if self.last.item==data:
                    self.last=None
            else:
                if self.last.next.item==data:
                    self.delete_first()
                else:
                    temp=self.last.next
                    while temp!=self.last:
                        if temp.next==self.last and self.last.item==data:
                            self.delete_last()
                            break
                        if temp.next.item==data:
                            temp.next=temp.next.next
                            break
                    
    def __iter__(self):
        if self.last==None:
            return CLLiterator(None)
        else:
            return CLLiterator(self.last.next)

class CLLiterator:
    def __init__(self,start):
        self.current=start
        self.start=start
        self.count=0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current==None:
            raise StopIteration
        if self.current==self.start and self.count==1:
            raise StopIteration
        else:
            self.count=1
        data=self.current.item
        self.current=self.current.next
        
        return data

        

class node: 
    def __init__(self,item=None,next=None):
        self.item=item
        self.next=next

a=last()
a.insert_at_start(20)
a.insert_at_last(30)
a.insert_after(a.search(20),90)
a.print_list()
print()
for i in a:
    print(i,end=' ')
