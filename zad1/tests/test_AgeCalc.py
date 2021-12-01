import unittest
import json

from sample.AgeCalc import *



class Test_ageCalc(unittest.TestCase):
	def test_from_file(self):
		self.temp = AgeCalc
		file = open("./ageCalc.json")
		testsData = json.load(file)
		file.close()
		for [input, expectedOutput] in testsData:
			self.assertEqual(self.temp.age(input[0], input[1]), expectedOutput)


if __name__ == "__main__":
	unittest.main()