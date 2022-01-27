class AutoList(list):
    def __init__(self, size=0, default=None):
        list.__init__(self)
        if default:
            self._default = default
        else:
            self._default = lambda:None
        self._expand(size)

    def check(self, index):
        return 0 <= index < len(self)

    def get(self, index):
        if self.check(index):
            return list.__getitem__(self, index)
        else:
            return None

    def _expand(self, size):
        while len(self) < size:
            self.append(self._default())

    def __getitem__(self, index):
        self._expand(index + 1)
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        self._expand(index + 1)
        return list.__setitem__(self, index, value)

if __name__ == '__main__':
    from test import check

    l1 = AutoList(2)
    check(l1, [None, None])

    check(l1.check(-1), False)
    check(l1.check(0), True)
    check(l1.check(1), True)
    check(l1.check(2), False)

    l1[0] = 1
    check(l1, [1, None])

    l1[4] = 2
    check(l1, [1, None, None, None, 2])
    check(l1.check(4), True)
    check(l1.check(5), False)

    check(l1.get(3), None)
    check(l1.get(4), 2)
    check(l1.get(5), None)
    check(l1.check(5), False)
    check(len(l1), 5)

    l2 = AutoList(2, list)
    check(l2, [[], []])
