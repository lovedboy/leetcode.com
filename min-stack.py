'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
'''

from array import array

class MinStack:

    def __init__(self):
      self.stack = array('i')
      self.min = array('i')

    # @param x, an integer
    # @return an integer
    def push(self, x):
        if not self.min:
            self.min.append(x)
        else:
            if x <= self.min[-1]:
                self.min.append(x)

        self.stack.append(x)
        return x

    # @return nothing
    def pop(self):
        x = self.stack.pop()
        if x == self.min[-1]:
            self.min.pop()


    # @return an integer
    def top(self):

        return self.stack[-1]
        

    # @return an integer
    def getMin(self):

        return self.min[-1]
