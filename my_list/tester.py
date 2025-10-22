from liste_rekursiv import ListeR
from liste_iterativ import ListeI

liste_r = ListeR()
liste_i = ListeI()
liste_p = list()

print("Listen frisch erstellt:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
# print(f"Erster Index der Listen gleich: {liste_r[0] == liste_i[0] == liste_p[0]}")
print(liste_r)
print(liste_i)
print(liste_p)


liste_r.append(0)
liste_i.append(0)
liste_p.append(0)

print(f"\nListen mit erstem Eintrag:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(f"Erster Index der Listen gleich: {liste_r[0] == liste_i[0] == liste_p[0]}")
print(liste_r)
print(liste_i)
print(liste_p)

for i in range(100):
    liste_r.append(i)
    liste_i.append(i)
    liste_p.append(i)

print(f"\nListen +100 Einträge:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(f"5. Index der Listen gleich: {liste_r[5] == liste_i[5] == liste_p[5]}")
print(liste_r)
print(liste_i)
print(liste_p)

for t in [None, 0, 0.0, 1 + 2j, True, "text", [1, 2, 3], (1, 2, 3), {1, 2, 3}, {"a": 1}, range(3), b"bytes",
          bytearray(b"bytes")]:
    liste_r.append(t)
    liste_i.append(t)
    liste_p.append(t)




print(f"\nListen mit den gängigen Datentypen:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(f"105. Index der Listen gleich: {liste_r[105] == liste_i[105] == liste_p[105]}")
print(liste_r)
print(liste_i)
print(liste_p)

liste_i[5] = "test"
liste_r[5] = "test"
liste_p[5] = "test"

print(f"\nÄnderung der Listen am Index 5:")
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(f"5. Index der Listen gleich: {liste_r[5] == liste_i[5] == liste_p[5]}")


print(liste_r)
print(liste_i)
print(liste_p)


print(f"\nTests mit negativem Index -10:")
print(liste_p[-10], liste_i[-10], liste_p[-10])
liste_p[-10] = "set_negative"
liste_i[-10] = "set_negative"
liste_r[-10] = "set_negative"
print(liste_p[-10], liste_i[-10], liste_p[-10])

print(liste_r)
print(liste_i)
print(liste_p)



liste_r_c = liste_r.copy()
liste_i_c = liste_i.copy()
liste_p_c = liste_p.copy()

print(f"\nKopierte Listen untereinander gleich und gleich den Originalen:")
print(f"Länge der kopierten Listen gleich: {len(liste_r_c) == len(liste_i_c) == len(liste_p_c)}")
print(f"Name der kopierten Listen gleich: {str(liste_r_c) == str(liste_i_c) == str(liste_p_c)}")
print(f"5. Index der kopierten Listen gleich: {liste_r_c[5] == liste_i_c[5] == liste_p_c[5]}")
print(f"Länge aller Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p) == len(liste_r_c) == len(liste_i_c) == len(liste_p_c)}")
print(f"Namen aller Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p) == str(liste_r_c) == str(liste_i_c) == str(liste_p_c)}")
print(f"5. Index aller Listen gleich: {liste_r[5] == liste_i[5] == liste_p[5] == liste_r_c[5] == liste_i_c[5] == liste_p_c[5]}")

print(liste_r)
print(liste_i)
print(liste_p)
print(liste_r_c)
print(liste_i_c)
print(liste_p_c)


liste_i[-7][1] = 5
print(f"Länge der Listen gleich: {len(liste_r) == len(liste_i) == len(liste_p)}")
print(f"Namen der Listen gleich: {str(liste_r) == str(liste_i) == str(liste_p)}")
print(liste_i)
print(liste_r)
print(liste_p)

liste_i_u = ListeI()
liste_i_u.append(1)
liste_i_u.append(1)
liste_i_u.append(1)
liste_i_u.append(2)
liste_i_u.append(2)
liste_i_u.append(2)
liste_i_u.append(2)
liste_i_u.append(2)
liste_i_u.append(3)
liste_i_u.append(3)
liste_i_u.append("test")
liste_i_u.append("test")
liste_i_u.append("test")

print(liste_i_u)
print(liste_i_u.unique_new())


for e in liste_i_u:
    print(e)