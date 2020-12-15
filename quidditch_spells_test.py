from potterworld.sub2 import quidditch as qd
from potterworld.sub2 import spells
import unittest

class TestQuidditch_Spells(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.spells = spells.spells()

    def setUp(self):
        print('setUp')
        self.rating = 0.9
        self.points = 50
        self.house = 'Gryffindor'
        
    def test_quidditch(self):
        self.assertIsInstance(qd.quidditch(self.rating, self.points, self.house), int)
        self.assertNotEqual(qd.quidditch(self.rating, self.points, self.house), 0)
        self.assertNotEqual(qd.quidditch(self.rating, self.points, self.house), self.points)
        self.assertEqual(qd.quidditch(self.rating, self.points, self.house)%10, 0)

    def test_spells(self):
        self.assertEqual(self.spells.spells_dict['Stupefy'], 'Stun your opponent.')
        self.assertEqual(self.spells.counter, 1)
        self.assertEqual(self.spells.get_all_spells(), self.spells.spells_dict)
        self.assertEqual(str(self.spells), 'This is the super Class for magical spells used at Hogwarts school.')

    def tearDown(self):
        print('tearDown')
        self.rating = 0
        self.points = 0
        self.house = 'None'

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        cls.spells.counter = 0

