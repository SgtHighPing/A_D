from typing import Any


class ListeR:
    class _Wagon:
        def __init__(self, value: Any):
            self.next = None
            self.value = value

        def __len__(self):
            if self.next is None:
                return 1
            else:
                return len(self.next) + 1

        def __repr__(self):
            if self.next is None:
                return repr(self.value)
            else:
                return repr(self.value) + ", " + repr(self.next)

        def getitem(self, index, counter=-1):
            counter += 1
            if counter == index:
                return self.value
            else:
                if self.next is not None:
                    return self.next.getitem(index, counter)
                else:
                    raise IndexError("Index out of range")

        def append(self, value):
            if self.next is None:
                self.next = ListeR._Wagon(value)
            else:
                self.next.append(value)

    def __init__(self):
        self._first = None

    def __str__(self) -> str:
        if self._first is None:
            return "[]"
        else:
            return f"[{repr(self._first)}]"

    def __len__(self):

        if self._first is None:
            return 0
        else:
            return len(self._first)

    def __getitem__(self, index):
        if self._first is None:
            raise IndexError("Index out of range")
        else:
            return self._first.getitem(index)

    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = ListeR._Wagon(value)
        else:
            self._first.append(value)
