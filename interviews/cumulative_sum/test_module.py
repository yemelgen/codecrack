#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R
import unittest
import pandas as pd
from solution import cumulative_reset_iterative, cumulative_reset_pandas


class TestCumulativeReset(unittest.TestCase):

    def setUp(self):
        self.example = [10, -4, 12, -16, 40, 50]
        self.expected = [0, -4, 0, -16, 0, 0]

    def test_iterative_solution(self):
        self.assertEqual(
            cumulative_reset_iterative(self.example),
            self.expected
        )

    def test_pandas_solution(self):
        result = list(cumulative_reset_pandas(pd.Series(self.example)))
        self.assertEqual(result, self.expected)

if __name__ == "__main__":
    unittest.main()
