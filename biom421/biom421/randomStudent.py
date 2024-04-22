#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 08:04:38 2024

@author: munsky
"""

import numpy as np

def chooseStudent(students, probs):
    # Ensure that probabilities sum to 1
    probs = probs / np.sum(probs)
    
    # Randomly select an entry based on the probability mass function
    student = np.random.choice(students, p=probs)
    
    # Get the index of the chosen entry
    index = students.index(student)
    
    return student, index