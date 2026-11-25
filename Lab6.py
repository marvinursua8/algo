class LLNode:
    def __init__(self,val):
        self.val = val
        self.next = None

    
    def length(self):
        counter = 0
        while self is not None:
            counter += 1
            self = self.next
        return counter

    def contains(self, val):
        while self is not None:
            if self.val == val:
                return True
            self = self.next
        return False

    
    def insert_after(self,val):
        new = LLNode(val)
        new.next = self.next
        self.next = new
        return new

    
    def remove_next(self):
        if self.next is None:
            return None  
        
        removed_node = self.next
        self.next = self.next.next  
        removed_node.next = None   
        return removed_node         

    
    def to_list(self):
        lst = []
        while self is not None:
            lst.append(self.val)
            self = self.next

        return lst
    
    def last(self):
        while self.next is not None:
            self = self.next
        return self

    def append(self, val):
        l = self.last()
        o = LLNode(val)
        l.next = o

    def find(self, val):
        while self is not None:
            if self.val == val:
                return self  
            self = self.next
        return None          


    def count(self,val):
        counter = 0
        while self is not None:
            if self.val == val:
                counter += 1
            self = self.next
        return counter

    def insert_after_value(self, target, val):
        target_node = self.find(target)
        if target_node is not None:
            return target_node.insert_after(val)
        return None

    def remove_next_after_value(self, target):
        target_node = self.find(target)

        if target_node is not None:
            return target_node.remove_next()
        return None





a = LLNode("A")
b = LLNode("B")
c = LLNode("C")
d = LLNode("D")

a.next = b
b.next = c
c.next = d

a.remove_next_after_value("B")

print(a.to_list())   