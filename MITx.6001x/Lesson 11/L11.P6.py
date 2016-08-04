#Lecture 11 Problem 6

class Queue(object):
    """A Queue isA queue is basically like a line at Disneyland
    you can add elements to a queue, and they maintain a specific order.
    When you want to get something off the end of a queue, you get the item
    that has been in there the longest (this is known as 
    'first-in-first-out', or FIFO). """
    
    def __init__(self):
        self.vals = []
        
    def insert(self,k):
        return self.vals.append(k)
    
    def remove(self):
        if self.vals == []:
            raise ValueError()
        else:
            return self.vals.pop(0)