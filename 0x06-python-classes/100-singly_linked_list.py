#!/usr/bin/python3
"""
This module contains 2 classes to define an instance of
a linked list in our program
"""


class Node():
    """
    This class is used to define an instance of a node
    of a linked list.
    """
    def __init__(self, data, next_node=None):
        self.__next_node = None
        if type(data) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = data
        if not isinstance(next_node, Node) and self.__next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = next_node
    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError("data must be an integer")
        else:
            self.__data = value
    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and self.__next_node is not None:
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList():
    """
    This class is used to define an instance of a signly linked list.
    """
    def __init__(self):
        self.__head = None
    def __str__(self):
        out = ""
        ptr = self.__head
        while ptr is not None:
            out += str(ptr.data)
            out += "\n"
            ptr = ptr.next_node
        return out
    def __repr__(self):
        return self.__str__()
    def sorted_insert(self, value):
        ptr = self.__head
        new_node = Node(value)
        if ptr is None:
            self.__head = new_node
        elif new_node.data <= self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            while ptr.next_node is not None:
                if new_node.data <= ptr.next_node.data:
                    break
                ptr = ptr.next_node
            new_node.next_node = ptr.next_node
            ptr.next_node = new_node
