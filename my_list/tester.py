from liste_rekursiv import ListeR
from liste_iterativ import ListeI

liste_r = ListeR()
liste_i = ListeI()
liste_p = list()

print("listen frisch erstellt:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Name der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(liste_r)
print(liste_i)
print(liste_p)


liste_r.append(0)
liste_i.append(0)
liste_p.append(0)

print(f"\nlisten mit erstem Eintrag:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Name der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(liste_r)
print(liste_i)
print(liste_p)

for i in range(100):
    liste_r.append(i)
    liste_i.append(i)
    liste_p.append(i)

print(f"\nlisten +100 Einträge:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Name der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(liste_r)
print(liste_i)
print(liste_p)

for t in [0, 0.0, 1 + 2j, True, "text", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"a": 1}, range(3), b"bytes",
          bytearray(b"bytes"), None]:
    liste_r.append(t)
    liste_i.append(t)
    liste_p.append(t)

print(f"\nlisten mit den gängigen Datentypen:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Name der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(liste_r)
print(liste_i)
print(liste_p)