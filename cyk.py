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
		table[i][i] = findRules(char)
		
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
		
word = 'baaba'
lw1 = len(word)+1
rules = {'S': ['AB','CA'],'A': ['BB','b'], 'B': ['CA','a'], 'C': ['AC','a']}
width = len(rules)*2+2
table = [[['-'] for x in range(lw1)] for x in range(lw1)] 
firstRowNCol()
diagonal()
combine()
drawLaTeX()   
