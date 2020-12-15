from potterworld.sub2 import learn_spells
from potterworld.sub2 import duel as dl
import unittest

class TestDuel_LearnSpells(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.learn_spells = learn_spells.learn_spells()
    
    def setUp(self):
        print('setUp')
        self.spell_keys_list = list(self.learn_spells.spells_dict.keys())

    def test_learn_spells(self):
        self.valid_set = ('l','r','u','d', 'random')
        self.assertEqual(self.learn_spells.spells_dict['Reparo'], 'Repair things that are broken.')
        self.assertIn(self.learn_spells.cast_a_spell(), self.spell_keys_list)
        pattern = self.learn_spells.get_wand_movement_pattern()
        print(pattern)
        if pattern == 'random':
            self.assertEqual(pattern, 'random')
        else:
            for i in pattern:
                self.assertIn(i, self.valid_set)

    def test_duel(self):
        self.wand_movement_pattern = 'random'
        self.assertIn(dl.duel_voldemort(self.wand_movement_pattern)[0], [0,1])
        self.assertIn(dl.duel_voldemort(self.wand_movement_pattern)[1], self.spell_keys_list)
        self.assertIn(dl.duel_voldemort(self.wand_movement_pattern)[2], self.spell_keys_list)
        self.assertEqual(len(dl.duel_voldemort(self.wand_movement_pattern)), 3)


    def tearDown(self):
        print('tearDown')
        self.spell_keys_list = None 

    @classmethod
    def tearDownClass(cls):
        print('teardownClass')
        cls.learn_spells = None
       
