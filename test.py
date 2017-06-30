from csv2md import csv2md

csv = 'column1,column2\nval1,val2\nval3,val4'

md = csv2md(csv)

assert md == '| column1 | column2 |\n|---------|---------|\n| val1    | val2    |\n| val3    | val4    |\n'

print(md)
