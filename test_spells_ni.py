from potterworld.sub2 import spells
import unittest

class Test_Spells(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.spells = spells.spells()

    def test_spells_one(self):
        self.assertEqual(self.spells.spells_dict['Stupefy'], 'Stun your opponent.')
        self.assertEqual(self.spells.counter, 1)
        self.assertEqual(self.spells.get_all_spells(), self.spells.spells_dict)
        self.assertEqual(str(self.spells), 'This is the super Class for magical spells used at Hogwarts school.')

    def test_spells_two(self):
        self.assertEqual(self.spells.spells_dict['Lumos'], 'Use your wand as a light.')
        self.assertEqual(self.spells.spells_dict['Nox'], 'Put out the light on your wand.')
        self.assertEqual(self.spells.spells_dict['Wingardium Leviosa'], 'Make things levitate')
        self.assertEqual(self.spells.spells_dict['Expecto Patronum'], 'Summons your patronus to repel evil dementors that want to suck out your soul. Should assign an animal to the patronus (eg. wolf, stag, bear, etc.).')
        self.assertEqual(self.spells.get_all_spells()['Accio'], 'Summons whatever you say after the spell to fly into your hand.')
    
    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        cls.spells.counter = 0

unittest.main()
    
