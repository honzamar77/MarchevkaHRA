# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
mistnosti = ["obývák", "chodba", "sklep", "trůnní sál"]
chodby = [[1, 2], [0], [0], [1, 2]]
zamcene_chodby = [[], [3], [], []]
klic = 2
zlato = [1, 0, 10, 300]

inventar = {"klic": False, "skore": 0}

hrac = 0
kroky = 0

def hotovo():
    return sum(zlato) == 0

while not hotovo():
    print("hráč je v místnosti:", mistnosti[hrac])
    print("hráč má", inventar["skore"], "zlata")
    print("zbývá zlata:", sum(zlato))

    kam_lze_jit = chodby[hrac]
    ok_vstupy = []

    for i, moznost in enumerate(kam_lze_jit):
        print("Moznost", i + 1, ": ", mistnosti[moznost])
        ok_vstupy.append(str(i + 1))

    if zlato[hrac] > 0:
        print("Moznost X : sebrat", zlato[hrac], "zlata")
        ok_vstupy.append("x")

    if hrac == klic:
        print("Moznost K : sebrat klíč")
        ok_vstupy.append("k")

    if inventar["klic"] and zamcene_chodby[hrac]:
        print("Moznost O : odemknout dveře ->", mistnosti[zamcene_chodby[hrac][-1]])
        ok_vstupy.append("o")

    vstup = input("> ")
    while not vstup in ok_vstupy:
        print("Špatný vstup.")
        vstup = input("> ")

    if vstup == "x":
        inventar["skore"] += zlato[hrac]
        zlato[hrac] = 0
    elif vstup == "k":
        inventar["klic"] = True
        klic = -1
    elif vstup == "o":
        cilova_mistnost = zamcene_chodby[hrac].pop()
        chodby[hrac].append(cilova_mistnost)
        print("Slyšíš jak cvaknul zámek a dveře se otevřely.")
    else:
        index_moznosti = int(vstup) - 1
        hrac = kam_lze_jit[index_moznosti]

    kroky += 1
    #break

print("Gratuluju, sebral jsi celkem,", inventar["skore"], "zlata za", kroky, "kroků")
