class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._queue = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self._queue.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        self._queue.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self._queue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self._queue) == 0
        