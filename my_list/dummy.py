import time
import random

def quicksort(l: list) -> list:
    if len(l) <= 1:
        return l

    pivot = l[0]
    links, rechts = [], []

    for z in l[1:]:
        if z < pivot:
            links.append(z)
        else:
            rechts.append(z)

    links = quicksort(links)
    rechts = quicksort(rechts)
    return links + [pivot] + rechts


def quicksort_inplace(l):

    def inner_sort(links, rechts):
        if links >= rechts:
            return

        pivot = l[links]
        i = links + 1
        j = rechts

        while True:
            while i <= j and l[i] < pivot:
                i += 1
            while i <= j and l[j] >= pivot:
                j -= 1

            if i >= j:
                break

            l[i], l[j] = l[j], l[i]

        l[links], l[j] = l[j], l[links]

        inner_sort(links, j - 1)
        inner_sort(j + 1, rechts)

    inner_sort(0, len(l) - 1)



def bubble_sort(liste):
    n = len(liste)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1,n):
            if liste[i - 1] > liste[i]:
                liste[i - 1], liste[i] = liste[i], liste[i - 1]
                swapped = True





n = 1000000
l = [random.randint(1, n) for x in range(n)]
l1 = l.copy()
l2 = l.copy()
#
# start = time.time()
# bubble_sort(l)
# print(f"Bubblesort: {time.time() - start}")

start = time.time()
quicksort(l1)
print(f"Quicksort: {time.time() - start}")

start = time.time()
quicksort_inplace(l2)
print(f"Quicksort in_place: {time.time() - start}")

# print(l)
# print(quicksort(l1))
# print(l2)

# assert l == quicksort(l1)
# assert l == l2


def quicksort_inplace(self) -> None:
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
