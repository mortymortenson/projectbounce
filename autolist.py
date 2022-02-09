import typing

Type = typing.TypeVar("Type")

class AutoList(list[Type]):
    """
    The AutoList works like a collections.defaultdict, but for list types.
    The primary use is for holding things that are mapped to SIDs, our
    sequential IDs, by holding them in List. Access methods will automatically
    extend the list.
    """
      
    def __init__(self, size: int=0, default: typing.Callable[[],Type]=None):
        """
        Create an AutoList, optionally specifying initial size and a callable
        for instantiating a default element.
        """
        list.__init__(self)
        if default:
            self._default = default
        else:
            self._default = lambda:None
        self._expand(size)

    def check(self, index: int) -> bool:
        """
        Checks if an index is within the bounds of this list.
        """
        return 0 <= index < len(self)

    def get(self, index: int) -> Type:
        """
        Gets the item at a specified index if it exists; otherwise returns
        None.
        """
        if self.check(index):
            return list.__getitem__(self, index)
        else:
            return None

    def _expand(self, size: int) -> None:
        """
        Expands this list to a new size.
        """
        while len(self) < size:
            self.append(self._default())

    def __getitem__(self, index: int) -> Type:
        self._expand(index + 1)
        return list.__getitem__(self, index)

    def __setitem__(self, index: int, value) -> None:
        self._expand(index + 1)
        return list.__setitem__(self, index, value)

def runTests():
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

if __name__ == '__main__':
    runTests()

