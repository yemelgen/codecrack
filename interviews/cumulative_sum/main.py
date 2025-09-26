#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

from solution import cumulative_reset_iterative, cumulative_reset_pandas
from unittest import main
import pandas as pd

# Demo run
example = pd.Series([10, -4, 12, -16, 40, 50])
print("Iterative:", cumulative_reset_iterative(example))
print("Pandas: ", list(cumulative_reset_pandas(example)))

# Run unit tests automatically
main(module='test_module', exit=False)
