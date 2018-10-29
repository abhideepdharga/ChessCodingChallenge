import __main__
import argparse
from argparse import ArgumentParser
from mock import patch
import sys
import test
from test import Chess
from test import Queen
import unittest


class TestTest(unittest.TestCase):
    def test_Factory(self):
    def test_findPossiblePosition(self):
        queen_instance = Queen()
        self.assertEqual(
            queen_instance.findPossiblePosition(position='D3',piece='QUEEN'),
            ['b1', 'd1', 'f1', 'c2', 'd2', 'e2', 'a3', 'b3', 'c3', 'e3', 'f3', 'g3', 'h3', 'c4', 'd4', 'e4', 'b5', 'd5', 'f5', 'a6', 'd6', 'g6', 'd7', 'h7', 'd8']
        )


    @patch.object(ArgumentParser, 'parse_args')
    @patch.object(ArgumentParser, '__init__')
    @patch.object(ArgumentParser, 'add_argument')
    def test_main(self, mock_add_argument, mock___init__, mock_parse_args):
        mock_add_argument.return_value = _StoreAction()
        mock___init__.return_value = None
        mock_parse_args.return_value = Namespace()
        self.assertEqual(
            __main__.main(),
            None
        )


    def test_setPosition(self):
        queen_instance = Queen()
        self.assertEqual(
            queen_instance.setPosition(position='D3',piece='QUEEN'),
            (4, 3)
        )


if __name__ == "__main__":
    unittest.main()
