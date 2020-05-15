import os
import sys
import csv

articles = []
with open(sys.argv[1], 'r') as f:
	reader = csv.reader(f)
	for line in list(reader)[1:]:
		columns = list(line)
		articles.append(columns[3]+"\n"+columns[4])

basename = sys.argv[2]
os.mkdir(basename)
for index, article in enumerate(articles):
	with open(basename + str(index) + '.txt', 'w') as of:
		print(article, file=of)    
        
