class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, value):
        if self.head is None:
            self.head = LinkedList.Node(value)
            self.tail = self.head
        else:
            self.tail.next = LinkedList.Node(value)
            self.tail = self.tail.next

    def get(self, index=0):
        if self.head is None:
            return None
        else:
            current = self.head
            while index > 0:
                current = current.next
                if current is None:
                    raise IndexError("Index out of range")
                index -= 1
            value = current.value
            return value

    def set(self, index, value):
        if self.head is None:
            raise IndexError("Index out of range")
        else:
            current = self.head
            while index > 0:
                current = current.next
                if current is None:
                    raise IndexError("Index out of range")
                index -= 1
            current.value = value

    def __str__(self):
        current = self.head
        values = []
        while current is not None:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)

    def __add__(self, other):
        if other is LinkedList:
            self.tail.next = other.head
            self.tail = other.tail
        else:
            self.tail.next = LinkedList.Node(other)
            self.tail = self.tail.next

    def __repr__(self):
        return self.__str__()

    @property
    def second(self):
        return self.get(1)

    @second.setter
    def second(self, value):
        self.set(1, value)

    class Node:
        def __init__(self, value):
            self.value = value
            self.next = None


li = LinkedList()
li.add(1)
li.add(5)
li.add(3)
