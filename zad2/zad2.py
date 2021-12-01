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


from parameterized import parameterized, parameterized_class
import unittest

class TestAgeCalc(unittest.TestCase):

    def setUp(self):
        self.temp = AgeCalc

    @parameterized.expand([
            ("Ziemia", 1000000000, 31.69),
            ("Merkury", 1000000000, 131.57),
            ("Wenus", 1000000000, 51.51),
            ("Mars", 1000000000, 16.85),
            ("Jowisz", 1000000000, 2.67)
    ])

    def test_parameterized(self, planet, sekundy, expectedOutput):
        self.assertEqual(self.temp.age(planet,sekundy) , expectedOutput)

    @parameterized.expand([
            ("Ziaa", 1000000000),
            ("Meeury", 1000000000),
            ("Wesus", 1000000000),
            ("Mars", None),
            ("Jowisz", [])
    ])

    def test_parameterized_exceptions(self, planet, sekundy):
        self.assertRaises(Exception, self.temp.age, planet, sekundy)

@parameterized_class(('planet', 'age', 'expectedOutput'), [
            ("Ziemia", 1000000000, 31.69),
            ("Merkury", 1000000000, 131.57),
            ("Wenus", 1000000000, 51.51),
            ("Mars", 1000000000, 16.85),
            ("Jowisz", 1000000000, 2.67)
    ])

class TestAgeCalcClass(unittest.TestCase):
    def setUp(self):
        self.temp = AgeCalc

    def test_parameterized_class(self):
        self.assertEqual(self.temp.age(self.planet, self.age), self.expectedOutput)

@parameterized_class(('planet', 'age'), [
            ("Ziaa", 1000000000),
            ("Meeury", 1000000000),
            ("Wesus", 1000000000),
            ("Mars", None),
            ("Jowisz", [])
    ])

class TestAgeCalcClassException(unittest.TestCase):
    def setUp(self):
        self.temp = AgeCalc

    def test_parameterized_class_exceptions(self):
        self.assertRaises(Exception, self.temp.age, self.planet, self.age)

if __name__ == '__main__':
    unittest.main()