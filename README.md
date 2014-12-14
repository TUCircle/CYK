# CYK


Create a CYK table for a special word and rules.

## How to use

- Install [Python](https://www.python.org/). 
- Start the programm with `python cyk.py`. 
- You will see a LaTeX table inside your console.
- Now you want to change the word and the rules which you have to do in the cyk.py file.
- `word = 'baaba'` -> here you can add your word.
- `rules = {'S': ['AB','CA'],'A': ['BB','b'], 'B': ['CA','a'], 'C': ['AC','a']}` 

This means:

- S -> AB | CA
- A -> BB | b
- B -> CA | a
- C -> AC | a

- If you want you can change the last line `drawLaTeX()` to `draw()` to draw a table inside the console without the special LaTeX syntax.
