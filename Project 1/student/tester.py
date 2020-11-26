# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:11:21 2020

@author: krlig
"""

import csv

with open('electronics.csv', newline='') as f:
    reader = csv.reader(f)
    your_list = list(reader)

print(your_list)
