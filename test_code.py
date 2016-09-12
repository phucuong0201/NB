  
import csv
import sys
from pprint import pprint
from collections import Counter

filename = open ('log.csv' , "r+")
reader = csv.reader(filename)
attack_line = 0
normal_line = 0
list_label  = []
list_time = []
count_time = 0
for line in reader:
    list_label.append(str(line[4]))
    list_time.append(str(line[0]))
for x in range(len(list_label)):
    if list_label[x] == '1':
        attack_line += 1
    if list_label[x] == '0':
        normal_line += 1
total_line = attack_line + normal_line
Pattack = float(attack_line)/float(total_line)
Pnormal = float(normal_line)/float(total_line)

pprint (Counter(list_time).items())