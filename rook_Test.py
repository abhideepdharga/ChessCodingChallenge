import __main__
import argparse
from argparse import ArgumentParser
from mock import patch
import sys
import test
from test import Chess
from test import Rook
import unittest


class TestTest(unittest.TestCase):
    def test_Factory(self):
    def test_findPossiblePosition(self):
        rook_instance = Rook()
        self.assertEqual(
            rook_instance.findPossiblePosition(position='D3',piece='ROOK'),
            ['d1', 'd2', 'a3', 'b3', 'c3', 'e3', 'f3', 'g3', 'h3', 'd4', 'd5', 'd6', 'd7', 'd8']
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
        rook_instance = Rook()
        self.assertEqual(
            rook_instance.setPosition(position='D3',piece='ROOK'),
            (4, 3)
        )


if __name__ == "__main__":
    unittest.main()
