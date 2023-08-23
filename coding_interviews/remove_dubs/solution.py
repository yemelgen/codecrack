#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

def remove_dups_v1( nums: list[int] ) -> list[int]:
    """ SC: O(n), TC: O(n*m) """
    result = []
    for n in nums:
        if n not in result:
            result.append(n)
    return result

def remove_dups_v2( nums: list[int] ) -> list[int]:
    """ SC: O(n), TC O(n + mlog(m)) """
    d = {}
    for i, n in enumerate(nums):
        d[n] = d.get(n, i)
    return sorted(d, key=d.get)

def remove_dups_v3( nums: list[int] ) -> list[int]:
    """ SC: O(n), TC: O(n) """
    d = {}
    for i, n in enumerate(nums):
        d[n] = d.get(n, i)
    return list(d.keys()) # works since 3.7

def remove_dups_v4( nums: list[int] ) -> list[int]:
    """ SC O(n), TC O(n)? because set operations is O(1) """
    s = set()
    result = []
    for n in nums:
        if n not in s:
            result.append(n)
        s.add(n)
    return result

remove_dups = remove_dups_v4
