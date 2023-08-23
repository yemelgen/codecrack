#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# pylint: disable=C,R

def find_overlaps_v1( array: list[tuple] ) -> list:
    """ My first attempt. Not working solution """
    result = set()
    for a in array:
        for b in [x for x in array if x != a ]:
            #print(a ,b )
            if  b[1] >= a[0] and b[0] <= a[1] :
                #print('yes')
                result.add(a)
            else:
                pass
                #print('no')
 
def find_overlaps_v2( intervals: list[tuple[int]] ) -> int:
    """ Working solution but O(n^2) """
    res = []
    for i, a in enumerate(intervals):
        for b in [ x for j, x in enumerate(intervals) if j != i ]:
            #if  b[1] >= a[0] and b[0] <= a[1] :
            if a[0] < b[1] and  a[1] > b[0]:
                res.append(a)
                break
    return res

def find_overlaps_v2_1( intervals:list[tuple[int]] ) -> int:
    """ Improved v2 solution, but still O(n^2) """
    if not intervals or len(intervals) == 1: return []

    overlaps = set()

    for i in range(0, len(intervals) ):
        for j in range(i + 1, len(intervals) ):
            if intervals[i][0] < intervals[j][1] and intervals[i][1] > intervals[j][0]:
                overlaps.add(i)
                overlaps.add(j)
    return [ x for i, x in enumerate(intervals) if i in overlaps ]


def find_overlaps_v3( intervals:list[tuple[int]] ) -> int:
    """ Working solution using hash maps. """
    if not intervals or len(intervals) == 1: return []

    count = {}

    for i in intervals:
        for r in range( i[0], i[1] + 1 ):
            count[r] = count.get( r, 0 ) + 1
    return [ i for i in intervals if any( r for r in range(i[0], i[1] + 1 ) if count[r] > 1) ]

def find_overlaps_v4( intervals:list[tuple[int]] ) -> int:
    """ Working solution O(n) or at least O(nlogn) """
    if not intervals or len(intervals) == 1: return []

    intervals.sort( key=lambda x: x[0] )
    overlaps = set()
    last_end = intervals[0][1]

    for i in range(1, len(intervals)):
        if intervals[i][0] <= last_end:
            overlaps.add(i)
            overlaps.add(i - 1)
        last_end = max(last_end, intervals[i][1])

    return [ x for i, x in enumerate(intervals) if i in overlaps ]

find_overlaps = find_overlaps_v4
