class Queue:
    """
    This file contains the implementation of Queue using the in-built Data Structure "List []" in python.
    Queue operates using FIFO (First In First Out) strategy. So the element that was added last will be
    popped first.
    "add_item" method allow adding objects to Queue
    "remove_item" method removes one element as per LIFO strategy
    "get_Queue" method displays the whole Queue
    "is_empty" method verifies if the Queue is empty or not and return True/False
    "peek" method displays the element that will be popped next
    "length" method displays the length of Queue
    """

    # Initialization of Queue Object
    def __init__(self):
        self.queue = []

    # add_item method allow adding objects to Queue
    def add_item(self, obj):
        self.queue.append(obj)

    # remove_item method removes one element as per FIFO strategy
    def remove_item(self):
        self.queue.pop(0)

    # get_queue method returns the whole Queue
    def get_queue(self):
        return self.queue

    # is_empty method verifies if the Queue is empty or not and return True/False
    def is_empty(self):
        return len(self.queue) == 0

    # peek method returns the element that will be popped next
    def peek(self):
        return self.queue[-1]

    # length method returns the length of Queue
    def length(self):
        return len(self.queue)
