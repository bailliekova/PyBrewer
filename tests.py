import unittest
from selector import BrewSelector
from brew import *
from collections import defaultdict

class SelectorTest(unittest.TestCase):
	#TODO: write test cases
	
	def setUp(self):
		self.empty_bs=BrewSelector(empty=True)
		self.brew_1=Brew('sequential', ['#F7FCFD', '#E5F5F9', '#CCECE6','#99D8C9', '#66C2A4', '#41AE76', '#238B45', '#006D2C', '#00441B'], 'BuGn', colorblind_safe=True)
		self.bs=BrewSelector() 

	def test_add_brew(self):
		self.empty_bs.add_brew(self.brew_1)
		self.assertEqual(self.empty_bs.brews, {'sequential':{9:{'BuGn':self.brew_1}}, 'diverging': defaultdict(dict), 'qualitative': defaultdict(dict)})

	def test_get_brew(self):
		self.assertEqual(self.bs.get_brew('sequential', 9, 'BuGn'), self.brew_1)

	def test_list_schemes(self):
		self.assertEqual(sorted(self.bs.list_schemes('sequential', 9)), sorted(('BuGn', 'BuPu', 'GnBu','OrRd', 'PuBu')))
	
	def test_get_colorblind_safe(self):
		raise Exception('write this test')

	def test_get_photocopy_safe(self):
		schemes=self.bs.list_schemes('sequential', 4, photocopy_safe=True)
		self.assertEqual(schemes, ('OrRd',))

	def test_get_print_safe(self):
		schemes=self.bs.list_schemes('sequential', 5, print_safe=True)
		self.assertEqual(schemes, ('GnBu',))

class BrewTest(unittest.TestCase):
	def test_rgb_to_hex(self):
		self.assertEqual('#FFFFFF', rgb_to_hex((255, 255, 255)))
		self.assertEqual('#FDD49E', rgb_to_hex((253, 212, 158)))

	def test_hex_to_rgb(self):
		self.assertEqual(hex_to_rgb('#FFFFFF'), (255, 255, 255))
		self.assertEqual(hex_to_rgb('#FDD49E'), (253, 212, 158))


if __name__=='__main__':
	unittest.main()