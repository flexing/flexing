# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 15:39:04 2017
"""
def factr(n):
	if n ==1:
		return 1
	else:
		return n*factr(n-1)
