#!/usr/bin/python3


SinglyLinkedList = __import__('100-singly_linked_list').SinglyLinkedList
Node = __import__('100-singly_linked_list').Node


#node = Node(3)
#print(node.data) #3
#print(node.next_node) #None
#newnode = Node(4)
#print(newnode.data) #4
#node.next_node = newnode
#print(node.next_node.data) #4
#newnode.data = 5
#print(node.next_node.data)
#newnode.next_node = "str"

sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(1)
sll.sorted_insert(0)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)
