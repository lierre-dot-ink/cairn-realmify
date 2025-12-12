import unittest
from cairn_realmify.cartographer import realmify
from cairn_realmify.territory import Territory


class TestCartographer(unittest.TestCase):
    def test_basic_rendering(self):
        t = Territory()
        string_map = realmify(t,width=64,height=32)

