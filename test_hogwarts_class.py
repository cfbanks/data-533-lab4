from potterworld import * 
import unittest

class mytest_hogwarts(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("\nsetUpClass\n")
        cls.student = Hogwarts("test_name")

    def setUp(self):
        print("\n------------------------------------------\nsetUp\n")
        self.student.name = "new_test_name"
        
    def test_attributes(self):
        print("\ntest attributes\n")
        self.assertEqual(self.student.name, "new_test_name")
        self.assertEqual(self.student.House, "no")
        self.assertEqual(self.student.hogwarts_houses_list, ['Gryffindor', 'Ravenclaw', 'Hufflepuff', 'Slytherin'])   
        self.assertEqual(self.student.default_quidditch_rating['Gryffindor'], 0.9)
        self.assertEqual(self.student.relic_list['Gryffindor'], "Sword of Gryffindor")
        self.assertEqual(self.student.ghost_list['Gryffindor'], "Nearly Headless Nick")
        self.assertEqual(self.student.mascot_list['Gryffindor'], "Lion")
        self.assertEqual(self.student.value_list['Gryffindor'], "Courage")        

    def test_gringotts(self):
        print("\ntest gringotts\n")
        self.student.gringotts(246.5)
        self.assertEqual(self.student.Golden_Galleons, 1)
        self.student.gringotts(14.5)
        self.assertEqual(self.student.Silver_Sickles, 1)
        self.student.gringotts(1.5)
        self.assertEqual(self.student.Bronze_Knuts, 3) 
        self.student.gringotts(2000)
        self.assertEqual(self.student.Golden_Galleons, 8)
        self.assertEqual(self.student.Silver_Sickles, 1)
        self.assertEqual(self.student.Bronze_Knuts, 27)          
        
    def test_get_wand(self):
        print("\ntest get_wand\n")
        self.student.gringotts(2000)
        (wood_type, core, length) = self.student.get_wand()
        self.assertIn(wood_type, ['Ash', 'Black Walnut', 'Cedar', 'Cherry', 'Elm', 'Hawthorn', 'Poplar', 'Red Oak', 'Sycamore', 'Walnut'])
        self.assertIn(core, ['Unicorn Hair', 'Dragon Heart String', 'Pheonix Feather'])
        self.assertIn(length, [9,10,11,12,13,14])

    def tearDown(self):
        print("\ntearDown\n------------------------------------------\n")

    @classmethod
    def tearDownClass(cls):
        print("tearDownClass\n")

unittest.main()
