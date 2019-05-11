from queue import PriorityQueue


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

        self.queue.queue.sort()
        result = self.binary_search(self.queue.queue, 0, len(self.queue.queue)-1, item.score)

        if result == -1:
            return False

        i = result
        while i > 0 and self.queue.queue[i-1][0] == item.score:
            i = i - 1

        j = result
        while j < len(self.queue.queue)-1 and self.queue.queue[j+1][0] == item.score:
            j = j + 1

        for element in self.queue.queue[i:j+1]:
            if item.state == element[2].state:
                return True
        return False

    def binary_search(self, arr, l, r, x):
        if r >= l:
            mid = int(l + (r - l)/2)

            if arr[mid][0] == x:
                return mid

            elif arr[mid][0] > x:
                return self.binary_search(arr, l, mid-1, x)

            else:
                return self.binary_search(arr, mid + 1, r, x)

        else:
            return -1
            pass
            
