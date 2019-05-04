from collections import deque
from queue import PriorityQueue
from functools import total_ordering


class Frontier:

    """Kuyruk yapısı LIFO ve FIFO olarak değerlendirebilir."""

    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        """Class için özel method, eleman olup olmadığı kontrol edilir."""

        for element in self.queue:
            if item.state == element.state:
                return True

        return False


class Explored:

    """AÇIKLAMA"""
    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        """Class için özel method, eleman olup olmadığı kontrol edilir."""

        for element in self.set:
            if item.state == element.state:
                return True

        return False


class Priority_Frontier:

    """Tupple olarak yerleştirilir düşük öncelikli olan pop edilir.(1,'bir')"""
    def __init__(self):
        self.queue = PriorityQueue()
        self.counter = 0

    def __contains__(self, item):
        """Class için özel method, eleman olup olmadığı kontrol edilir."""

        for element in self.queue:
            if item.state == element.state:
                return True

        return False
