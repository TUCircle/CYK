# CYK


Create a CYK table for a special word and rules.

## How to use

- Install [Python](https://www.python.org/). 
- Start the programm with `python cyk.py "abba"`. 
- You will see a table inside your console for the word `"abba"` and the given rules inside the `config.py` file.
- If you want to change the rules you need to change the `config.py` file which is in the same directory.
- `rules = {'S': ['AB','CA'],'A': ['BB','b'], 'B': ['CA','a'], 'C': ['AC','a']}` 
- If you want you can print the table as a latex table with `python cyk.py "abba" --latex`
