from potterworld import * 
import unittest

class mytest_hogwarts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.student = Hogwarts("test_name")
        cls.spells = spells()
        cls.learn_spells = learn_spells()
        cls.my = Wizard("Batman")

    def setUp(self):
        print("\n------------------------------------------\nsetUp\n")
        self.student.name = "new_test_name"
        self.spell_keys_list = list(self.learn_spells.spells_dict.keys())
        
    def test_attributes(self):
        print("\ntest attributes\n")
        self.assertEqual(self.student.House, "no")
        self.assertEqual(self.student.hogwarts_houses_list, ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])   
        self.assertEqual(self.student.default_quidditch_rating['Gryffindor'], 0.9)
        self.assertEqual(self.student.relic_list['Gryffindor'], "Sword of Gryffindor")
        self.assertEqual(self.student.ghost_list['Gryffindor'], "Nearly Headless Nick")
        self.assertEqual(self.student.mascot_list['Gryffindor'], "Lion")
        self.assertEqual(self.student.value_list['Gryffindor'], "Courage")        

    def test_gringotts(self):
        print("\ntest gringotts\n")
        self.student.gringotts("test")
        self.student.gringotts(246.5)
        self.assertEqual(self.student.Golden_Galleons, 1)
        self.student.gringotts(14.5)
        self.assertEqual(self.student.Silver_Sickles, 1)
        self.student.gringotts(0.5)
        self.assertEqual(self.student.Bronze_Knuts, 1) 
        self.student.gringotts(2000)
        self.assertEqual(self.student.Golden_Galleons, 8)
        self.assertEqual(self.student.Silver_Sickles, 1)
        self.assertEqual(self.student.Bronze_Knuts, 27)          
        
    def test_get_wand(self):
        print_song()
        print("\ntest get_wand\n")
        self.student.gringotts(246.5)
        (wood_type, core, length) = self.student.get_wand()
        self.student.gringotts(14.5)
        (wood_type, core, length) = self.student.get_wand()
        self.student.gringotts(0.5)
        (wood_type, core, length) = self.student.get_wand()        
        self.assertIn(wood_type, ['Ash', 'Black Walnut', 'Cedar', 'Cherry', 'Elm', 'Hawthorn', 'Poplar', 'Red Oak', 'Sycamore', 'Walnut'])
        self.assertIn(core, ['Unicorn Hair', 'Dragon Heart String', 'Pheonix Feather'])
        self.assertIn(length, [9,10,11,12,13,14])
        
    def test_spells(self):
        self.assertEqual(self.spells.spells_dict['Stupefy'], 'Stun your opponent.')
        self.assertEqual(self.spells.counter, 1)
        self.assertEqual(self.spells.get_all_spells(), self.spells.spells_dict)
        self.assertEqual(str(self.spells), 'This is the super Class for magical spells used at Hogwarts school.')         

    def test_quidditch(self):
        self.assertIsInstance(quidditch(1, 50, 'Gryffindor'), int) 
        self.assertIsInstance(quidditch(0, 50, 'Gryffindor'), int) 
        self.assertIsInstance(quidditch(1, 50, 'Gryffindor'), int)
        self.assertNotEqual(quidditch(1, 50, 'Gryffindor'), 0)
        self.assertNotEqual(quidditch(0, 50, 'Gryffindor'), 50)
        self.assertEqual(quidditch(0, 50, 'Gryffindor')%10, 0)  
        self.assertNotEqual(quidditch(1, 50, 'Gryffindor'), 0)
        self.assertNotEqual(quidditch(0, 50, 'Ravenclaw'), 0)
        self.assertNotEqual(quidditch(1, 50, 'Hufflepuff'), 0)
        self.assertNotEqual(quidditch(0, 50, 'Slytherin'), 0)  
        
    def test_learn_spells(self):
        self.valid_set = ('l','r','u','d', 'random')
        self.assertEqual(self.learn_spells.spells_dict['Reparo'], 'Repair things that are broken.')
        self.assertIn(self.learn_spells.cast_a_spell(), self.spell_keys_list)
        pattern = self.learn_spells.get_wand_movement_pattern()
        print(pattern)
        pattern = self.learn_spells.get_wand_movement_pattern()
        print(pattern)
        print('\nenter valid characters\n')
        pattern = self.learn_spells.get_wand_movement_pattern()
        print(pattern)
        for i in pattern:
            self.assertIn(i, self.valid_set) 
                
    def test_duel(self):
        self.my.wand_movement_pattern = 'random'
        self.my.learn_spells_flag = 0
        duel_voldemort(self.my.wand_movement_pattern)
        self.my.learn_spells_flag = 1
        self.my.wand_movement_pattern = 'random'
        duel_voldemort(self.my.wand_movement_pattern)
        self.my.wand_movement_pattern = 'lrud'
        self.assertIn(duel_voldemort(self.my.wand_movement_pattern)[0], [0,1])
        self.assertIn(duel_voldemort(self.my.wand_movement_pattern)[1], self.spell_keys_list)
        self.assertIn(duel_voldemort(self.my.wand_movement_pattern)[2], self.spell_keys_list)
        self.assertEqual(len(duel_voldemort(self.my.wand_movement_pattern)), 3)

    def test_gringotts_inherited(self):
        print("\ntest currency exchange in gringotts using inheritance\n")
        self.my.gringotts(246.5)
        self.assertEqual(self.my.Golden_Galleons, 1)
        self.my.gringotts(14.5)
        self.assertEqual(self.my.Silver_Sickles, 1)
        self.my.gringotts(0.5)
        self.assertEqual(self.my.Bronze_Knuts, 1)         
        self.my.gringotts(2000)
        self.assertEqual(self.my.Golden_Galleons, 8)
        self.assertEqual(self.my.Silver_Sickles, 1)
        self.assertEqual(self.my.Bronze_Knuts, 27)

    def test_get_wand_inherited(self):
        print("\ntest get_wand using inheritance\n")
        self.my.night_crawl()
        self.my.get_wand()
        self.my.night_crawl()
        self.assertIn(self.my.wand_wood_type, ['Ash', 'Black Walnut', 'Cedar', 'Cherry', 'Elm', 'Hawthorn', 'Poplar', 'Red Oak', 'Sycamore', 'Walnut'])
        self.assertIn(self.my.wand_core, ['Unicorn Hair', 'Dragon Heart String', 'Pheonix Feather'])
        self.assertIn(self.my.wand_length, [9,10,11,12,13,14])        
        
    def test_house(self):
        print("\ntest house using sorting_hat()\n")
        self.my.sorting_hat()
        print(self.my.House)
        self.my.House = 'no'
        self.my.sorting_hat()
        self.my.learn_spells_flag = 0
        self.my.display()
        self.my.learn_spells_flag = 1
        self.my.display()          
        self.assertIn(self.my.House, ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])
        self.assertIn(self.my.house_quidditch_rating, [0.9, 0.7, 0.6])
        self.assertIn(self.my.house_mascot, ['Lion', 'Eagle', 'Badger', 'Serpent'])
        self.assertIn(self.my.house_ghost, ['Nearly Headless Nick', 'The Grey Lady', 'The Fat Friar', 'The Bloody Baron'])
          
                 
    def tearDown(self):
        print("\ntearDown\n------------------------------------------\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")

unittest.main()
