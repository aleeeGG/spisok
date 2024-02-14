class LinkedList:

    class Item:
        value = None
        next = None

        def __init__(self, value):
            self.value = value

    head: Item = None
    __count: int = 0

    @property
    def count(self):
        index = -1
        current = self.head
        while current:
            current = current.next
            index +=1
        self.__count = index
        return self.__count

    def append_begin(self, value):
        item = LinkedList.Item(value)
        item.next = self.head
        self.head = item

    def append_end(self, value):
        current = self.head
        if current is None:
            self.head = LinkedList.Item(value)
            return

        while current.next:
            current = current.next
        item = LinkedList.Item(value)
        current.next = item
 
 
    def remove_first(self):
        '''Удаление первого элемента списка'''
        if self.head is None:
            raise ValueError("Список пуст")
        self.head = self.head.next
 
    def remove_last(self):  
        '''удаление последнего элемента'''
        if self.head is None:
            raise ValueError("Список пуст")  
        current = self.head  
        pred = None  
     
        while current.next is not None:  
            pred = current  
            current = current.next  
     
        if pred is None:  
            self.head = None  
        else:  
            pred.next = None 
 
 
    def remove_at(self, index):
        '''удаление по индексу'''
        if self.head is None:
            raise ValueError("Список пуст")
        if index < 0:
            raise ValueError("index не может быть меньше 0")
        if index == 0:
            self.head = self.head.next
            return

        current = self.head
        pred = None
        ind = 0

        while ind < index and current is not None:
            pred = current
            current = current.next
            ind += 1

        if current is None:
            raise ValueError("Такого индекста не существует")

        pred.next = current.next
        current.next = None


 
 
 
 
    def remove_first_value(self,rm):             
        '''удаление по значению превого элемента''' 
        if self.head is None:
            raise ValueError("Список пуст")
        current = self.head 
 
        if current is not None: 
            if current.value==rm: 
                self.head = current.next 
                current = None 
                return 
        while current is not None: 
            if current.value==rm: 
                break 
            last = current 
            current = current.next 
        if current == None: 
            return 
        last.next = current.next 
        current = None 
 
 
    def remove_last_value(self,rm): 
        '''удаление по значению последнего элемента'''
        if self.head is None:
            raise ValueError("Список пуст")
        current = self.head   
        pred = None  
      
        while current.next is not None:  
            if current.next.value == rm:  
                pred = current  
            current = current.next  
     
        if pred is not None:  
            pred.next = pred.next.next  
            return  
 
