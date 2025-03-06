#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 10:30:21 2025

@author: brooklynndominguez
"""

def convert_roman_numerals(s):
    count = 0
    for i, char in enumerate(s):
        if char== "I":
            if len(s) > i +1 and s[i+1] == "V":
                return 4
            elif len(s) > i +1 and s[i+1] == "X":
                return 9
            count +=1
        elif char=="V":
            count +=5
        elif char == "X":
            count +=10
    return count


