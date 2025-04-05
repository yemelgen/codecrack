#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

import unittest
from solution import remove_dups

class Test( unittest.TestCase ):
    def test_case1(self):
        a = [20, 21, 0, 18, 0, 2, 4, 3, 2, 1, 1]
        b = [20, 21, 0, 18, 2, 4, 3, 1]
        self.assertEqual( remove_dups(a), b )

if __name__ == '__main__':
    unittest.main()
