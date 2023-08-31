class Stack:
    """
    This file contains the implementation of Stack using the in-built Data Structure "List []" in python.
    Stack operates using LIFO (Last In First Out) strategy. So the element that was added last will be
    popped first.

    "add_item" method allow adding objects to Stack
    "remove_item" method removes one element as per LIFO strategy
    "get_stack" method displays the whole Stack
    "is_empty" method verifies if the Stack is empty or not and return True/False
    "peek" method displays the element that will be popped next in Stack
    "length" method displays the length of Stack
    """

    # Initialization of Stack Object
    def __init__(self):
        self.stack = []

    # add_item method allow adding objects to Stack
    def add_item(self, obj):
        self.stack.append(obj)

    # remove_item method removes one element as per LIFO strategy
    def remove_item(self):
        self.stack.pop()

    # get_stack method returns the whole Stack
    def get_stack(self):
        return self.stack

    # is_empty method verifies if the Stack is empty or not and return True/False
    def is_empty(self):
        return len(self.stack) == 0

    # peek method returns the element that will be popped next
    def peek(self):
        return self.stack[-1]

    # length method returns the length of Stack
    def length(self):
        return len(self.stack)
