import unittest
from main import parse_args, generate_filename
from freezegun import freeze_time


class TestMain(unittest.TestCase):
    def test_parse_args(self):
        # full arg names:
        input_args1 = ['--input', 'input.json', '--output', 'output.json']
        result1 = parse_args(args=input_args1)
        self.assertEqual('input.json', result1.input)
        self.assertEqual('output.json', result1.output)

        # short arg names:
        input_args2 = ['-i', 'input.json', '-o', 'output.json']
        result2 = parse_args(args=input_args2)
        self.assertEqual('input.json', result2.input)
        self.assertEqual('output.json', result2.output)

        # not all args provided in command line:
        input_args3 = ['-i', 'input.json']
        with self.assertRaises(BaseException):
            parse_args(input_args3)

    @freeze_time("2012-01-01")
    def test_generate_filename(self):
        self.assertEqual('myfile_2012-01-01.dat', generate_filename('myfile_%d.dat'))

