import unittest
from main import parse_args


class TestMain(unittest.TestCase):
    def test_parse_args(self):
        input_args1 = ['--input', 'input.json', '--output', 'output.json']
        result1 = parse_args(args=input_args1)
        self.assertEqual('input.json', result1.input)
        self.assertEqual('output.json', result1.output)

        input_args2 = ['-i', 'input.json', '-o', 'output.json']
        result2 = parse_args(args=input_args2)
        self.assertEqual('input.json', result2.input)
        self.assertEqual('output.json', result2.output)
