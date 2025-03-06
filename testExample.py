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
        
    def test_V(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("V"), 5)
    
    def test_IV(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("IV"), 4)
        
    def test_VI(self):
        from roman import convert_roman_numerals
        self.assertEqual(convert_roman_numerals("VI"), 6)
        
    def test_X(self):
       from roman import convert_roman_numerals
       self.assertEqual(convert_roman_numerals("X"), 10) 
        

if __name__ == '__main__':
    unittest.main()

