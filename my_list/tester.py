from git.a_d import meineliste

liste_meine = meineliste.Liste()

liste_python = list()

# print(liste_meine)
# print(liste_python)

if str(liste_meine) != str(liste_python):
    print("Alarm, es ist nicht gleich")

assert str(liste_meine) == str(liste_python), "es ist nicht gleich"
print("hat alles geklappt")