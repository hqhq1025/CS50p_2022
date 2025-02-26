class Jar:
    def __init__(self, capacity=12):
        if capacity < 0 or not isinstance(capacity,int):
            raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return self._cookies*"🍪"

    def deposit(self, n):
        if self._cookies + n >self._capacity or not isinstance(n,int) or n < 0:
            raise ValueError
        else:
            self._cookies += n

    def withdraw(self, n):
        if self._cookies - n < 0 or not isinstance(n,int) or n < 0:
            raise ValueError
        else:
            self._cookies -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._cookies