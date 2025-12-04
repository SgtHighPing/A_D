from typing import Any
import time, random


class Liste:
    class _Wagon:
        def __init__(self, value):
            self.next = None
            self.value = value

        def __repr__(self):
            return repr(self.value)

    # ab hier die Listeninterna

    def __init__(self, iterable=None):
        self._first = None
        self._last = None
        if iterable is not None:
            self.extend_ohne_cheat(iterable)


    def __contains__(self, item):  # nativer Support für den "in"-Operator (ohne Fallback auf iter oder getitem)
        for elem in self:
            if elem == item:
                return True
        return False

    def __iter__(self):  # Generator-Methode, nativer Support von Iteration via iter/next (ohne Fallback auf getitem)
        wagon = self._first
        while wagon is not None:
            yield wagon.value
            wagon = wagon.next

    def __getitem__(self, index):  # indizierter lesender Zugriff
        if type(index) is not int:
            raise TypeError("Index muss ein int sein")
        if index < 0 or self._first is None:  # index negativ oder Liste leer
            raise IndexError("list index out of range")  # das ist die kopierte Meldung der Python-Liste

        schaffner = self._first
        while index > 0:
            schaffner = schaffner.next
            if schaffner is None:
                raise IndexError("list index out of range")
            index -= 1
        return schaffner.value

    def __len__(self) -> int:  # len
        if self._first is None:
            return 0
        else:
            schaffner = self._first
            counter = 1
            while schaffner.next is not None:
                schaffner = schaffner.next
                counter += 1
            return counter

    def __repr__(self):  # repr und str
        if self._first is None:
            return "[]"
        ergebnis = repr(self._first)
        schaffner = self._first
        while schaffner.next is not None:
            schaffner = schaffner.next
            ergebnis += f", {repr(schaffner)}"
        return f"[{ergebnis}]"

    def __setitem__(self, index: int, wert: Any) -> None:
        if type(index) is not int:
            raise TypeError("Index muss ein int sein")
        if index < 0 or self._first is None:  # index negativ oder Liste leer
            raise IndexError("list index out of range")  # das ist die kopierte Meldung der Python-Liste
        schaffner = self._first
        while index > 0:
            schaffner = schaffner.next
            if schaffner is None:
                raise IndexError("list index out of range")
            index -= 1
        schaffner.value = wert

    def extend(self, iterable):
        if not iterable:
            return

        if self._first is None:
            it = iter(iterable)
            try:
                first = next(it)
            except StopIteration:
                return
            self._first = Liste._Wagon(first)
            self._last = self._first
            for value in it:
                self._last.next = Liste._Wagon(value)
                self._last = self._last.next
            return

        for value in iterable:
            self._last.next = Liste._Wagon(value)
            self._last = self._last.next

    def extend_ohne_cheat(self, iterable):
        if not iterable:
            return

        if self._first is None:
            it = iter(iterable)
            try:
                first_value = next(it)
            except StopIteration:
                return
            self._first = Liste._Wagon(first_value)
            current = self._first
            for value in it:
                current.next = Liste._Wagon(value)
                current = current.next
            return

        current = self._first
        while current.next is not None:
            current = current.next

        for value in iterable:
            current.next = Liste._Wagon(value)
            current = current.next

    def append(self, value: Any):
        if self._first is None:
            self._first = Liste._Wagon(value)
            self._last = self._first
        else:
            self._last.next = Liste._Wagon(value)
            self._last = self._last.next

    def copy(self):
        kopie = Liste()
        for elem in self:
            kopie.append(elem)
        return kopie

    def sort_bubble(self):
        '''
        Bubble sort
        :return: nix, sortiert in-place
        '''
        swapped = True
        while swapped:
            swapped = False
            schaffner1 = self._first
            if schaffner1 is not None:
                schaffner2 = schaffner1.next
                while schaffner2 is not None:
                    if schaffner1.value > schaffner2.value:
                        schaffner1.value, schaffner2.value = schaffner2.value, schaffner1.value
                        swapped = True
                    schaffner1 = schaffner2
                    schaffner2 = schaffner2.next

    def sort_bubble_try(self):
        '''
        wie das "normale" Bubblesort, statt aber in jedem Schritt jeweils explizit zu prüfen, ob das Listenende
        erreicht ist, wird stumpf immer weiter gemacht, bis ein Fehler geworfen wird. Das funktioniert auch
        und spart ggf. Zeit (hier bei uns spart es ein ganz klein wenig Zeit im einstelligen Prozent-Bereich)
        :return: nix, sortiert in-place
        '''
        swapped = True
        while swapped:
            swapped = False
            schaffner1 = self._first
            if schaffner1 is not None:
                schaffner2 = schaffner1.next
                try:
                    while True:
                        if schaffner1.value > schaffner2.value:
                            schaffner1.value, schaffner2.value = schaffner2.value, schaffner1.value
                            swapped = True
                        schaffner1 = schaffner2
                        schaffner2 = schaffner2.next
                except (TypeError, AttributeError):
                    pass

    def sort_bubble_array(self):
        '''
        Bubblesort mit direkter Indizierung, so, als ob unsere Liste ein Array wäre
        Dadurch kann man den Standard-Algorithmus direkt hier umsetzen
        es wird funktionieren, es wird aber schrecklich langsam sein!!!
        erfordert __getitem__ und __setitem__ damit die lesenden und schreibenden Zugriffe per Index möglich sind
        :return: nix, sortiert in-place
        '''
        n = len(self)
        swapped = True
        while swapped:  # wurde im letzten Durchlauf getauscht? (auch das ist schon eine Optimierung)
            swapped = False
            for i in range(1, n):  # ein Durchlauf aller Paare
                if self[i - 1] > self[i]:  # größeres vor kleinerem?
                    self[i - 1], self[i] = self[i], self[i - 1]  # tauschen
                    swapped = True
            n -= 1  # Optimierung (fertig sortierte Elemente am oberen Ende werden nicht erneut betrachtet)

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
        def _partition(start: "Liste._Wagon", end: "Liste._Wagon | None") -> "Liste._Wagon":
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

    def unique(self):
        """
        ©️Beesten
        in-place, entfernt doppelt auftretende Elemente
        :return: nichts, es wird dir originale Liste (self) verändert
        """
        schaffner = self._first
        while schaffner is not None:
            vorgaenger = schaffner
            kontroletti = schaffner.next
            while kontroletti is not None:
                nachfolger = kontroletti.next
                if kontroletti.value == schaffner.value:
                    vorgaenger.next = nachfolger
                else:
                    vorgaenger = kontroletti
                kontroletti = nachfolger
            schaffner = schaffner.next
        return


if __name__ == '__main__':
    n = 5000
    l = []
    li1 = Liste()


    for i in range(n):
        r = random.randint(0,n)
        l.append(r)
    li1.extend_ohne_cheat(l)
    li2 = li1.copy()
    li2.extend_ohne_cheat([])
    print("Befüllen fertig")
    # assert str(l) == str(li1)
    # assert str(l) == str(li2)

    start = time.time()
    l.sort()
    print(f"Dauer PowerSort bei {n} Elementen: ", time.time()-start)
    start = time.time()
    li1.sort_quick_marco()
    print(f"Dauer QuickSort Marco bei {n} Elementen: ", time.time()-start)
    start = time.time()
    li2.quicksort_inplace_chatgpt()
    print(f"Dauer QuickSort ChatGPT bei {n} Elementen: ", time.time()-start)
    li2.append(2)

