from typing import Any

class ListeI:

    class _Wagon:
        def __init__(self, value: Any):
            self.next = None
            self.value = value

    def __init__(self):
        self._first = None

    def __str__(self) -> str:

        if self._first is None:
            return "[]"
        else:
            mein_inhalt = "["
            if self._first.next is None:
                mein_inhalt = mein_inhalt + repr(self._first.value) + "]"
                return mein_inhalt
            else:
                ich_bin = self._first.next
                mein_inhalt = mein_inhalt + repr(ich_bin.value) + ", "
                while ich_bin.next is not None:
                    mein_inhalt = mein_inhalt + repr(ich_bin.value) +", "
                    ich_bin = ich_bin.next
                return mein_inhalt + repr(ich_bin.value) + "]"


    def __len__(self):

        if self._first is None:
            return 0
        else:
            ich_bin = self._first
            counter = 1
            while ich_bin.next is not None:
                ich_bin = ich_bin.next
                counter+=1
            return counter

    def __getitem__(self, index: int):
        if type(index) is not int:
            raise TypeError(f"Index muss ein Int sein und kein {type(index)}")
        if index < 0:
            index = len(self) + index
        if self._first is None:
            raise IndexError("Index außerhalb der möglichen Reichweite")
        else:
            ich_bin = self._first
            counter = 0
            while ich_bin is not None:
                if counter == index:
                    return ich_bin.value
                ich_bin = ich_bin.next
                counter+=1
            raise IndexError("Index außerhalb der möglichen Reichweite")

    def __setitem__(self, index: int, value: Any):
        if type(index) is not int:
            raise TypeError(f"Index muss ein Int sein und kein {type(index)}")
        if index < 0:
            index = len(self) + index
        if self._first is None:
            raise IndexError("Index außerhalb der möglichen Reichweite")
        else:
            ich_bin = self._first
            counter = 0
            while ich_bin is not None:
                if counter == index:
                    ich_bin.value = value
                    return None
                ich_bin = ich_bin.next
                counter+=1
            raise IndexError("Index außerhalb der möglichen Reichweite")


    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = ListeI._Wagon(value)
        else:
            schaffner = self._first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = ListeI._Wagon(value)

    def copy(self):
        liste_copy = ListeI()
        if self._first is None:
            return liste_copy
        else:
            ich_bin = self._first
            while ich_bin is not None:
                liste_copy.append(ich_bin.value)
                ich_bin = ich_bin.next
            return liste_copy



