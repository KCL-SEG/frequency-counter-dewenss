"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    count = 0
    for i in items:
        item_str = str(i)
        if item_str in frequencies:
            frequencies[item_str]+= 1
        else:
            frequencies[item_str] = 1
    print(frequencies)
    return frequencies

frequencies(["a","b","a","a"])