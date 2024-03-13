from all_characters import all_characters

all_characters_names = []
print("Wähle den Helden mit dem du Spielen möchtest")
for charcacter in all_characters:
    all_characters_names.append(charcacter.name)
print(all_characters_names)


def choose_start_hero():
    not_choosen = True
    while not_choosen:
        choose = input(":")
        if choose in all_characters_names:
            print(f"Herforragend, das du dich für {choose} entscheiden hast")
            not_choosen = False
        else:
            print("Nochmal...")


choose_start_hero()
