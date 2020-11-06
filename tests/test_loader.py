import json
import unittest
from pathlib import Path

from myaml.loader import safe_load

YAML_DIR = Path(__file__).resolve().parent / 'yaml'


class TestLoader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_simple(self):
        out = safe_load(YAML_DIR / 'simple.yaml')

        ref = [
            {'x1': {'x': 4, 'y': 0}},
            {'x2': {'x': 7, 'y': 5}}
        ]

        self.assertTrue(isinstance(out, list))
        self.assertEqual(len(out), 2)

        for o, r in zip(out, ref):
            self.assertDictEqual(o, r)