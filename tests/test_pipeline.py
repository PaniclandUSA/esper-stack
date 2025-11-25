import unittest

from vse import Crystallizer
from chronocore import NarrativeEngine
from pictogram import Compositor


class TestEsperPipeline(unittest.TestCase):

    def test_full_pipeline(self):
        vse_expr = {
            "polarity": "calm",
            "deictic": "decl",
            "scope": "one",
            "certainty": "cert",
            "tau": 0.8,
            "intent": {"axis": "hello"},
        }

        vse_out = Crystallizer().process(vse_expr)
        self.assertEqual(vse_out["stage"], "vse")

        cc_out = NarrativeEngine().sequence(vse_out)
        self.assertEqual(cc_out["stage"], "chronocore")

        pg_out = Compositor().render(cc_out)
        self.assertEqual(pg_out["stage"], "pictogram")
        self.assertIn("glyph", pg_out)

    def test_intent_propagation(self):
        expr = Crystallizer().process({"intent": {"axis": "warn"}})
        cc = NarrativeEngine().sequence(expr)
        pg = Compositor().render(cc)
        self.assertEqual(pg["glyph"], "[WARN-Glyph]")


if __name__ == "__main__":
    unittest.main()
