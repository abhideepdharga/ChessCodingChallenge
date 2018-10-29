import __main__
import argparse
from argparse import ArgumentParser
from mock import patch
import sys
import test
from test import Chess
from test import Knight
import unittest


class TestTest(unittest.TestCase):
    def test_Factory(self):
    def test_findPossiblePosition(self):
        knight_instance = Knight()
        self.assertEqual(
            knight_instance.findPossiblePosition(position='D3',piece='KNIGHT'),
            ['c1', 'e1', 'b2', 'f2', 'b4', 'f4', 'c5', 'e5']
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
        knight_instance = Knight()
        self.assertEqual(
            knight_instance.setPosition(position='D3',piece='KNIGHT'),
            (4, 3)
        )


if __name__ == "__main__":
    unittest.main()
