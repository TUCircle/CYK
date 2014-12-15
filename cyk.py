#!/usr/bin/env python
#-*- coding: utf-8 -*-
# cyk.py - Cocke-Younger-Kasami implementation in python
# 
# Copyright (c) 2014 by 
# Ole Kroeger <echo by5rcm9lZ2VyQHdpa3VuaWEuZGUK | base64 -d>
# Christian Rebischke <echo Q2hyaXMuUmViaXNjaGtlQGdtYWlsLmNvbQo= | base64 -d>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/
#
#====================================================================== 
# Author: Ole Kroeger
# Email : echo by5rcm9lZ2VyQHdpa3VuaWEuZGUK | base64 -d
# Github: www.github.com/Wikunia
#
# Author: Christian Rebischke
# Email : echo Q2hyaXMuUmViaXNjaGtlQGdtYWlsLmNvbQo= | base64 -d
# Github: www.github.com/Shibumi
#
# vim: set ts=2 sts=2 sw=2 et
#

import argparse

def firstRowNCol():
	# first row
	for c in range(1,lw1):
		table[0][c] = [word[c-1]]
	# first col
	for r in range(1,lw1):
		table[r][0] = [word[r-1]]

def diagonal():
	for i in range(1,lw1):
		char = word[i-1]
		rules = findRules(char)
		if len(rules) == 0:
			print("It isn't possible to create a '"+char+"' with the given rules.")
			exit(1)
		table[i][i] = rules
		
def findRules(endString):
	starts = []
	for start,end in rules.items():
		for rule in end:
			if rule == endString:
				starts.append(start)
	return starts
	
def possibleCombs(a,b):
	combs = []
	for i in range(len(a)):
		if a[i] != '-':
			for j in range(len(b)):
				if b[j] != '-':
					add = str(a[i])+str(b[j])
					if (add not in combs):
						combs.append(add)
	return combs
			
def combine():
	n = len(word)
	for h in range(1,n):
		for i in range(1,n-h+1):
			starts = []
			for j in range(i,i+h):
				allEnds = possibleCombs(table[j][i],table[i+h][j+1])
				if allEnds:
					for end in allEnds:
						for rule in findRules(end):
							if rule not in starts:
								starts.append(rule)
			if starts:
				table[i+h][i] = starts
			
def draw():
	for r in range(lw1):
		row = ''
		for c in range(lw1):
			if table[r][c][0] == table[r][c][0].lower(): 
				rowStr = table[r][c][0]
			else:
				rowStr = '{'+','.join(table[r][c])+'}'
			row += '|'+rowStr+' '*(width-len(rowStr))
		print(row)	
		
def drawLaTeX():
	print('\\'+'begin{tabular}{'+'|c'*lw1+'|} \hline')
	for r in range(lw1):
		row = ''
		for c in range(lw1):
			if table[r][c][0] == table[r][c][0].lower(): 
				rowStr = table[r][c][0]
			else:
				rowStr = '\{'+','.join(table[r][c])+'\}'
			if (c != 0):
				row += '& '
			row += rowStr+' '*(width-len(rowStr))
		print(row + '   \\\\ \hline') 
	print('\end{tabular}')
		


parser = argparse.ArgumentParser()
parser.add_argument("word", help='Your word that you wish to test')
parser.add_argument("--latex", help="draw output in LateX", action="store_true")
args = parser.parse_args()
word = args.word
lw1 = len(word)+1
try:
  from config import *
except ImportError:
  print('No config.py')
  exit(1)
width = len(rules)*2+2
table = [[['-'] for x in range(lw1)] for x in range(lw1)] 
firstRowNCol()
diagonal()
combine()
if args.latex:
  drawLaTeX()
else:
  draw()
