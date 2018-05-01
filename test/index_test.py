import unittest2 as unittest
from ipynb.fs.full.index import *

class TestObjectAttributes(unittest.TestCase):

    def test_school_class(self):
        self.assertEqual(type(school), type(School("example school")))

    def test_school_roster_method(self):
        example = School("example school")
        self.assertEqual(example.roster(), {})

    def test_school_add_student_method(self):
        example = School("example school")
        example.add_student("Napolean Dynamite", 11)
        self.assertItemsEqual(example.roster(), {11: ["Napolean Dynamite"]})

    def test_school_grade_method(self):
        example = School("example school")
        example.add_student("Napolean Dynamite", 11)
        example.add_student("Pedro", 11)
        example.add_student("Deb", 11)
        self.assertItemsEqual(example.grade(11), ["Napolean Dynamite", "Pedro", "Deb"])

    def test_school_sort_roster_method(self):
        example = School("example school")
        example.add_student("Napolean Dynamite", 11)
        example.add_student("Pedro", 11)
        example.add_student("Deb", 11)
        example.add_student("Ron Burgundy", 10)
        example.add_student("Veronica Corningstone", 10)
        example.add_student("Brick Tamland", 10)
        example.add_student("Brian Fantana", 9)
        self.assertItemsEqual(example.sort_roster(), {11: ["Pedro", "Deb", "Napolean Dynamite"], 10: ["Brick Tamland", "Ron Burgundy", "Veronica Corningstone"], 9: ["Brian Fantana"]})
