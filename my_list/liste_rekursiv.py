from typing import Any
import random
import time


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
                    raise IndexError("Index außerhalb der möglichen Reichweite")

        def setitem(self, index, value, counter=-1):
            counter += 1
            if counter == index:
                self.value = value
                return None
            else:
                if self.next is not None:
                    return self.next.setitem(index, value, counter)
                else:
                    raise IndexError("Index außerhalb der möglichen Reichweite")

        def append(self, value):
            if self.next is None:
                self.next = ListeR._Wagon(value)
            else:
                self.next.append(value)

        def copy(self, liste_copy: "ListeR"):
            liste_copy.append(self.value)
            if self.next is None:
                return liste_copy
            else:
                return self.next.copy(liste_copy)

    def sort_quick_marco(self):
        def quicksort(links, rechts):
            if links is rechts: return
            pivot = links.value  # Pivot
            aktuell = links  # aktuell Untersuchter
            vorgrenze = links  # Vorgänger von Obergrenze
            grenze = links  # Oberster, der kleiner/gleich dem Pivot ist
            while True:
                aktuell = aktuell.next
                if aktuell is rechts: break
                if aktuell.value < pivot:
                    vorgrenze = grenze
                    grenze = grenze.next
                    grenze.value, aktuell.value = aktuell.value, grenze.value
            links.value, grenze.value = grenze.value, links.value
            if grenze is not rechts:
                vorgrenze = grenze
                grenze = grenze.next
            quicksort(links, vorgrenze)
            quicksort(grenze, rechts)

        quicksort(self._first, None)

    def quicksort_inplace_chatgpt(self) -> None:
        """Sortiert die Liste in-place mit QuickSort (arbeitet direkt auf den Wagons)."""

        # Hilfsfunktion: partitioniert den Bereich [start, end)
        def _partition(start: "ListeR._Wagon", end: "ListeR._Wagon | None") -> "ListeR._Wagon":
            pivot_value = start.value
            p = start  # letzte Position eines Elements < pivot
            q = start.next  # läuft durch den Rest der Liste

            while q is not end:
                if q.value < pivot_value:
                    p = p.next
                    # Werte tauschen, nicht die Knoten selbst
                    p.value, q.value = q.value, p.value
                q = q.next

            # Pivot an die richtige Stelle bringen
            start.value, p.value = p.value, start.value
            return p  # p zeigt jetzt auf den Pivot-Knoten an finaler Position

        # Rekursive QuickSort-Funktion auf dem Bereich [start, end)
        def _quicksort(start: "ListeR._Wagon | None", end: "ListeR._Wagon | None") -> None:
            # 0 oder 1 Element im Bereich -> schon sortiert
            if start is None or start is end or start.next is end:
                return

            pivot_node = _partition(start, end)
            _quicksort(start, pivot_node)  # linker Teil
            _quicksort(pivot_node.next, end)  # rechter Teil

        # leere Liste oder 1 Element -> nichts zu tun
        if self._first is None or self._first.next is None:
            return

        _quicksort(self._first, None)

    def bubble_sort_nl2(self):
        '''Bubble Sort zwischen Originaler und neuer Liste'''
        nl = ListeR()
        schaffner = self._first

        while schaffner is not None:
            wagon = self._Wagon(schaffner.value)

            if nl._first is None or wagon.value < nl._first.value:
                wagon.next = nl._first
                nl._first = wagon
            else:

                kontroletti = nl._first
                while kontroletti.next is not None and kontroletti.next.value <= wagon.value:
                    kontroletti = kontroletti.next

                wagon.next = kontroletti.next
                kontroletti.next = wagon

            schaffner = schaffner.next

        return nl

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
        if type(index) is not int:
            raise TypeError(f"Index muss ein Int sein und kein {type(index)}")
        if index < 0:
            index = len(self) + index
        if self._first is None:
            raise IndexError("Index außerhalb der möglichen Reichweite")
        else:
            return self._first.getitem(index)

    def __setitem__(self, index, value):
        if type(index) is not int:
            raise TypeError(f"Index muss ein Int sein und kein {type(index)}")
        if index < 0:
            index = len(self) + index
        if self._first is None:
            raise IndexError("Index außerhalb der möglichen Reichweite")
        else:
            return self._first.setitem(index, value)

    def append(self, value: Any) -> None:
        if self._first is None:
            self._first = ListeR._Wagon(value)
        else:
            self._first.append(value)

    def copy(self):
        liste_copy = ListeR()
        if self._first is None:
            return liste_copy
        else:
            return self._first.copy(liste_copy)



if __name__ == '__main__':
    n = 1000
    l = []
    lm = ListeR()
    lc = ListeR()

    for i in range(n):
        r = random.randint(0,n)
        l.append(r)
        lm.append(r)
        lc.append(r)

    assert str(l) == str(lm)
    assert str(l) == str(lc)

    start = time.time()
    l.sort()
    print(f"Dauer PowerSort bei {n} Elementen: ", time.time()-start)
    start = time.time()
    lm.sort_quick_marco()
    print(f"Dauer QuickSort Marco bei {n} Elementen: ", time.time()-start)
    start = time.time()
    lc.quicksort_inplace_chatgpt()
    print(f"Dauer QuickSort ChatGPT bei {n} Elementen: ", time.time()-start)
