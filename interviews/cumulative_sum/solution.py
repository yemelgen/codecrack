#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R
""" Solution to the cumulative sum problem. """

import pandas as pd


def cumulative_reset_iterative(series):
    """
    Iterative solution.
    Given a series of integers, compute the cumulative sum,
    but reset to 0 whenever the sum becomes positive.
    """
    res = []
    cur = 0
    for value in series:
        cur += value
        if cur > 0:
            cur = 0
        res.append(cur)
    return res


def cumulative_reset_pandas(series):
    """ Vectorized Pandas solution using cumsum and cummax. """
    series = pd.Series(series)
    return series.cumsum() - series.cumsum().cummax()
