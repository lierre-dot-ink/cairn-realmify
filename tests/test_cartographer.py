import unittest
from cairn_realmify.cartographer import realmify
from cairn_realmify.territory import Territory, generate_territory


class TestCartographer(unittest.TestCase):

    def test_basic_rendering(self):
        t = generate_territory({})

        arbitrary_width = 64
        arbitrary_height = 32

        realm = realmify(t,width=arbitrary_width,height=arbitrary_height)

        lines = realm.splitlines()

        self.assertEqual(arbitrary_height,len(lines))
        for l in lines:
            self.assertEqual(arbitrary_width,len(l))


    def test_expected_territory(self):
        config = {
                "A": ("Silver_Face",(0.25,0.25)),
                "B": ("Broken_Sundial",(0.25,0.75)),
                "C": ("Silver_Face",(0.75,0.75)),
        }
        t = generate_territory(config)
        realm = realmify(t,12,4,filler_char="·")

        expected_realm = "\n".join(["············",
        "···A·····B··",
        "············",
        "·········C··"])

        self.assertEqual(realm,expected_realm)

