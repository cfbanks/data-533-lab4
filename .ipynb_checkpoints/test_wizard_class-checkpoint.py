from potterworld import * 
import unittest

class mytest_wizard(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.my = Wizard("Batman")

    def setUp(self):
        print("\n------------------------------------------\nsetUp\n")
        self.my.name = "new_test_name"

    def test_gringotts(self):
        print("\ntest currency exchange in gringotts using inheritance\n")
        self.my.gringotts(246.5)
        self.assertEqual(self.my.Golden_Galleons, 1)
        self.my.gringotts(14.5)
        self.assertEqual(self.my.Silver_Sickles, 1)
        try:
            self.my.gringotts(0.5)
        except InsufficientBalance:
            print('Insufficien tBalance')
        self.my.gringotts(1)
        self.assertEqual(self.my.Bronze_Knuts, 2)         
        self.my.gringotts(2000)
        self.assertEqual(self.my.Golden_Galleons, 8)
        self.assertEqual(self.my.Silver_Sickles, 1)
        self.assertEqual(self.my.Bronze_Knuts, 27)

    def test_get_wand(self):
        print("\ntest get_wand using inheritance\n")
        self.assertEqual(self.my.name, "new_test_name")
        self.my.get_wand()
        self.assertIn(self.my.wand_wood_type, ['Ash', 'Black Walnut', 'Cedar', 'Cherry', 'Elm', 'Hawthorn', 'Poplar', 'Red Oak', 'Sycamore', 'Walnut'])
        self.assertIn(self.my.wand_core, ['Unicorn Hair', 'Dragon Heart String', 'Pheonix Feather'])
        self.assertIn(self.my.wand_length, [9,10,11,12,13,14])        
        
    def test_house(self):
        print("\ntest house using sorting_hat()\n")
        self.my.sorting_hat()
        self.assertIn(self.my.House, ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])
        self.assertIn(self.my.house_quidditch_rating, [0.9, 0.7, 0.6])
        self.assertIn(self.my.house_mascot, ['Lion', 'Eagle', 'Badger', 'Serpent'])
        self.assertIn(self.my.house_ghost, ['Nearly Headless Nick', 'The Grey Lady', 'The Fat Friar', 'The Bloody Baron'])
        
    def test_learn_spells(self):
        print("\ntest learn spells\n")
        self.my.learn_spells()
        self.assertEqual(self.my.learn_spells_flag, 1)
        wand_movement_pattern = self.my.wand_movement_pattern
        pattern_check = False
        if wand_movement_pattern == 'random':
            pattern_check = True
        else:
            pattern_check = True
            for char in set(list(wand_movement_pattern)):
                if char not in ['l','r','u','d']:
                    pattern_check = False
        self.assertEqual(pattern_check, True)

    def tearDown(self):
        print("\ntearDown\n------------------------------------------\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")

unittest.main()
