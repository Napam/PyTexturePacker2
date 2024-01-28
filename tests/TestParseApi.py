import unittest
from PyTexturePacker.Rect import Rect
from PyTexturePacker.MaxRectsPacker.MaxRectsPacker import MaxRectsPacker


class TestNewParseApi(unittest.TestCase):
    def test_parse(self):
        packer = MaxRectsPacker()
        rect = Rect(0, 0, 5, 1)
        result = packer.pack([rect])

