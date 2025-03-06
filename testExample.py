#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 09:50:58 2025

@author: brooklynndominguez
"""

import unittest

class TestRoman(unittest.TestCase):
    def test_I(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("I"), 1)

    def test_II(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("II"), 2) 
    
    def test_III(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("III"), 3)
        

if __name__ == '__main__':
    unittest.main()

