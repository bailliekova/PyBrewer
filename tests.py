import unittest
from selector import BrewSelector
from brew import Brew
from collections import defaultdict

class SelectorTest(unittest.TestCase):
	#TODO: write test cases
	
	def setUp(self):
		self.bs=BrewSelector()
		self.brew_1=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn', colorblind_safe=True)
	
	def test_add_brew(self):
		self.bs.add_brew(self.brew_1)
		self.assertEqual(self.bs.brews, {'sequential':{9:{'BuGn':self.brew_1}}, 'diverging': defaultdict(dict), 'qualitative': defaultdict(dict)})

	def test_get_brew(self):
		raise Exception('write this test')

	def test_get_default_brew(self):
		raise Exception('write this test')
	
	def test_get_colorblind_safe(self):
		raise Exception('write this test')

	def test_get_photocopy_safe(self):
		raise Exception('write this test')

	def test_get_printer_friendly(self):
		raise Exception('write this test')

if __name__=='__main__':
	unittest.main()