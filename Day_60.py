print('Day 60: Implementation of linked list\n')

#Single Linked List
class SingleLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.nextSingleLinkedList = None

a = SingleLinkedList(1)
b = SingleLinkedList(2)
c = SingleLinkedList(3)

a.nextSingleLinkedList = b
b.nextSingleLinkedList = c

print('Single Linked List:')
print(a.nextSingleLinkedList.value)
print(b.nextSingleLinkedList.value)






#Double Linked List
class DoubleLinkedList(object):

    def __init__(self, value):
        self.value = value
        self.nextSingleLinkedList = None
        self.prevSingleLinkedList = None


a = DoubleLinkedList(1)
b = DoubleLinkedList(2)
c = DoubleLinkedList(3)

a.nextSingleLinkedList = b
b.prevSingleLinkedList = a
b.nextSingleLinkedList = c
c.prevSingleLinkedList = b

print('\nDouble Linked List:')
print(a.nextSingleLinkedList.value)
print(b.prevSingleLinkedList.value)

