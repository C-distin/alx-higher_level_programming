#!/usr/bin/python3
"""
Define a Node class for a singly linked list.
"""


class Node:
    """
    A Node class that defines a singly linked list
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node

        Args:
                data: the data to store in the node
                next_node: the next node in the list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """
        Get the data stored in the node
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data stored in the node

        Args:
                value: the data to store in the node
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """
        Get the next node in the list
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node in the list

        Args:
                value: the next node in the list
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


"""
Define a SinglyLinkedList class for a singly linked list.
"""


class SinglyLinkedList:
    """
    A SinglyLinkedList class that defines a singly linked list
    """

    def __init__(self):
        """
        Initialize a new SinglyLinkedList
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new node into a singly linked list

        Args:
                value: the data to store in the new node
        """
        if self.__head is None:
            self.__head = Node(value)
            return
        if value < self.__head.data:
            self.__head = Node(value, self.__head)
            return
        current = self.__head
        while current.next_node is not None and value > current.next_node.data:
            current = current.next_node
        current.next_node = Node(value, current.next_node)

    def __str__(self):
        """
        Return the representation of a singly linked list
        """
        current = self.__head
        string = ''
        while current is not None:
            string += str(current.data) + '\n'
            current = current.next_node
        return string
