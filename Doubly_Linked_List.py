class dll:

    def __init__(self,start=None):
        self.start=start

    def isempty(self):
        return self.start==None
    
    def insert_at_start(self,data):
        n=node(data,self.start,None)
        if not self.isempty():
            self.start.prev=n
        self.start=n

    def insert_at_last(self,data):
        temp=self.start
        if self.start!=None:
            while temp.next is not None:
                temp=temp.next
        n=node(data,None,temp)
        if temp==None:
            self.start=n
        else:
            temp.next=n

    def search(self,data):
        temp=self.start
        while temp is not None:
            if temp.item==data:
                return temp
            temp-temp.next
        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=node(data,temp.next,temp)
            if temp.next is not None:
                temp.next.prev=n
            temp.next=n

    def print_list(self):
        temp=self.start
        while temp is not None:
            print(temp.item,end=' ')
            temp=temp.next

    def delete_first(self):
        if self.start is not None:
            self.start=self.start.next
            if self.start is not None:
                self.start.prev=None

    def delete_last(self):
        if self.start==None:
            pass
        elif self.start.next==None:
            self.start=None
        else:
            temp=self.start
            while temp.next is not None:
                 temp=temp.next
            temp.prev.next=None

    def delete_data(self,data):
        if self.start==None:
            pass
        else:
            temp=self.start
            while temp is not None:
                if temp.item==data:
                    if temp.next is not None:
                        temp.next.prev=temp.prev
                    if temp.prev is not None:
                        temp.prev.next=temp.next
                    else:
                        self.start=temp.next
                    break
                temp=temp.next

    def __iter__(self):
        return dlliterator(self.start)

class dlliterator:

    def __init__(self,start):
        self.current=start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data=self.current.item
        self.current=self.current.next
        return data

class node:
    def __init__(self,item=None,next=None,prev=None):
        self.item=item
        self.next=next
        self.prev=prev


a=dll()
a.insert_at_start(20)
a.insert_at_last(23)
a.insert_after(a.search(20),15)
a.delete_first()
for i in a:
    print(i,end=" ")
print( )
