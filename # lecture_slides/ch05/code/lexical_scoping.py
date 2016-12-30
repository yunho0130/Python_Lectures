# -*- coding: utf-8 -*-
"""
Created on Fri Dec 30 07:16:41 2016

@author: Yunho
"""

def get_adder(summand1):
    """Returns a function that adds numbers to a given number."""
    def adder(summand2):
        return summand1 + summand2

    return adder