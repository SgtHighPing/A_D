from typing import Any

class Liste:
    def __init__(self):
        self._first = None


    def __str__(self) -> str:
        def wer_bin_ich(wagon: Wagon) -> str:
            if wagon.next is None:
                return str(wagon)
            return str(wagon) + ", " + wer_bin_ich(wagon.next)

        if self._first is None:
            return "[]"
        else:
            return "[" + wer_bin_ich(self._first) + "]"

    def __len__(self):

        if self._first is None:
            return 0
        return len(self._first)
        # def len_rekursiv(wagon: Wagon):
        #     if wagon.next is None:
        #         return 1
        #
        #     return len_rekursiv(wagon.next) + 1
        #
        # if self.first is None:
        #     return 0
        # return len_rekursiv(self.first)

        # def len_rekursiv(wagon: Wagon, counter:int) -> int:
        #     if wagon.next is None:
        #         return counter + 1
        #
        #     return len_rekursiv(wagon.next, counter + 1)
        # if self.first is None:
        #     return 0
        # return len_rekursiv(self.first, 0)
        #
        #
        # #
        # # else:
        # #     schaffner = self.first
        # #     counter = 1
        # #     while schaffner.next is not None:
        # #         schaffner = schaffner.next
        # #         counter+=1
        # #     return counter

    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = Wagon(value)
        else:
            schaffner = self._first
            while schaffner.next is not None:
                schaffner = schaffner.next
            schaffner.next = Wagon(value)



class Wagon:
    def __init__(self,value: Any):
        self.next = None
        self.value = value

    def __len__(self, counter:int):
        if self.next is None:
            return 1
        return len(self.next) + 1

    def __repr__(self):
        return f"Wagon({self.value})"
