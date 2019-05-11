from collections import deque
from queue import PriorityQueue


class Frontier:

    """Kuyruk yapısı LIFO ve FIFO olarak değerlendirebilir."""

    def __init__(self):
        self.queue = deque()

    def __contains__(self, item):
        """Class için özel method, eleman olup olmadığı kontrol edilir."""
        """if a in Frotier_objesi() sorgusunu yapmamızı sağlar"""

        for element in self.queue:
            if item.state == element.state:
                return True

        return False


class Explored:

    """Daha önce baktıgımız durumları tutmak icin kullandığımız structures"""
    def __init__(self):
        self.set = set()

    def __contains__(self, item):
        """Class için özel method, eleman olup olmadığı kontrol edilir."""
        """if a in Frotier_objesi() sorgusunu yapmamızı sağlar"""

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
