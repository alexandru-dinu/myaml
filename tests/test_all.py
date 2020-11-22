import json
import unittest
from pathlib import Path

from myaml.myaml import safe_load, dump

YAML_DIR = Path(__file__).resolve().parent / 'yaml'


class TestLoader(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def assertCorrect(self, file_name, target):
        out = safe_load(file_name)

        self.assertIsInstance(out, list)
        self.assertEqual(len(out), len(target))

        for o, t in zip(out, target):
            self.assertDictEqual(o, t)

    def test_simple(self):
        target = [
            {'x1': {'x': 4, 'y': 0}},
            {'x2': {'x': 7, 'y': -0.056315}},
            {'x3': {
                'x': 'hello world',
                'y': '/this/is/a/path'
            }}
        ]

        self.assertCorrect(YAML_DIR / 'simple.yaml', target)

    def test_nested(self):
        target = [{
            'level1': {
                'x': 4,
                'y': 0,
                'level2': {
                    'x': 7,
                    'y': -0.056315,
                    'level3': {
                        'x': 'hello world',
                        'y': '/this/is/a/path'
                    }
                }
            }
        }]

        self.assertCorrect(YAML_DIR / 'nested.yaml', target)
