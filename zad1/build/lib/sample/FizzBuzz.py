class AgeCalc:
    def age(planeta, sekundy):
        planety = ["Ziemia", "Merkury", "Wenus", "Mars", "Jowisz", "Saturn", "Uran", "Neptun"]

        if (type(sekundy) != int):
            if type(sekundy) == str:
                sekundy = float(sekundy)
                sekundy = int(sekundy)
            if type(sekundy) == float:
                sekundy = int(sekundy)
            elif type(sekundy) != int:
                raise Exception(
                    "Niewspierane wejście w jednostce czasu. Proszę podać czas w sekundach jako liczbę np. 100000000")

        if (sekundy < 0):
            raise Exception("Czas nie może być ujemny")

        if planeta not in planety:
            raise Exception("Podane wyrażenie nie jest wspieraną planetą.")

        if (planeta == "Ziemia"):
            lata = round(sekundy / 31557600, 2)
        if (planeta == "Merkury"):
            lata = round(sekundy / 31557600 / 0.2408467, 2)
        if (planeta == "Wenus"):
            lata = round(sekundy / 31557600 / 0.61519726, 2)
        if (planeta == "Mars"):
            lata = round(sekundy / 31557600 / 1.8808158, 2)
        if (planeta == "Jowisz"):
            lata = round(sekundy / 31557600 / 11.862615, 2)
        if (planeta == "Saturn"):
            lata = round(sekundy / 31557600 / 29.447498, 2)
        if (planeta == "Uran"):
            lata = round(sekundy / 31557600 / 84.016846, 2)
        if (planeta == "Neptun"):
            lata = round(sekundy / 31557600 / 164.79132, 2)

        return lata