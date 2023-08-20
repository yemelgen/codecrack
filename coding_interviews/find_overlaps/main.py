#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

# This entrypoint file 
from solution import find_overlaps
from unittest import main

# Test your function by calling it here
find_overlaps([ (1, 10), (15, 20), (101, 110) ])

# Run unit tests automatically
main(module='test_module', exit=False)
