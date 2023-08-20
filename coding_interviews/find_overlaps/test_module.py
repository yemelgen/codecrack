#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R
from solution import find_overlaps
import unittest

class Test( unittest.TestCase ):
    def test_case1( self ):
        a = [ (1, 10), (15, 20), (101, 110), ]
        b = []
        self.assertCountEqual( find_overlaps(a), b )

    def test_case2( self ):
        a = [ (1, 10),(15, 20), (101, 110),(18, 22), ]
        b = [ (15, 20), (18, 22), ]
        self.assertCountEqual( find_overlaps(a), b )

    def test_case3( self ):
        a = [ (1, 10), (15, 20), (101, 110), (1, 10), (1, 10), (105, 120), ]
        b = [ (1, 10), (1, 10), (1, 10), (101, 110), (105, 120), ]
        self.assertCountEqual( find_overlaps(a), b )

    def test_case4( self ):
        a = [ (1, 10), (15, 20), (101, 110), (18, 30), (27, 35), ]
        b = [ (15, 20), (18, 30), (27, 35), ]
        self.assertCountEqual( find_overlaps(a), b )

    def test_case5( self ):
        a = [ (5, 10), (301, 400), (180, 200), (100, 300), (120, 150), (160, 170), (195, 220), ]
        b = [ (180, 200), (100, 300), (120, 150), (160, 170), (195, 220), ]
        self.assertCountEqual( find_overlaps(a), b )

if __name__ == '__main__':
    unittest.main()
