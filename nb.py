import csv
import sys
from pprint import pprint
from collections import Counter

attack_line = 0
normal_line = 0
log_line = []
query_list = []
time_list_attack = []
time_list_normal = []
ptime_attack = []
ptime_normal = []
method_list_attack = []
method_list_normal = []
pmethod_attack = []
pmethod_normal = []
query_list_attack = []
query_list_normal = []
pquery_attack = []
pquery_normal = []
status_list_attack = []
status_list_normal = []
pstatus_attack = []
pstatus_normal = []
time_label_attack = []
time_label_normal = []
status_label_attack = []
status_label_normal = []
method_label_attack = []
method_label_normal = []
query_label_attack = []
query_label_normal = []
time_compare_attack = []
time_compare_normal = []
status_compare_attack = []
status_compare_normal = []
method_compare_attack = []
method_compare_normal = []
query_compare_attack = []
query_compare_normal = []
with open('log.csv' , "r+") as csvlogfile:
    reader_log = csv.reader(csvlogfile)
    for line in reader_log:
        log_line.append(str(line[4]))
    for x in range(len(log_line)):
        if log_line[x] == '1':
            attack_line += 1
        if log_line[x] == '0':
            normal_line +=1
    total_line = attack_line + normal_line
    pattack = float(attack_line)/float(total_line)
    pnormal = float(normal_line)/float(total_line)
csvlogfile.close()

with open('attack_log.csv' , "r+") as csv_attackfile:
    reader_attacklog = csv.reader(csv_attackfile)
    for line in reader_attacklog:
        time_list_attack.append(str(line[0]))
        method_list_attack.append(str(line[1]))
        query_list_attack.append(str(line[2]))
        status_list_attack.append(str(line[3]))
count_time_attack = Counter(time_list_attack).values()      #time
count_time_attack_items = Counter(time_list_attack).items()
count_method_attack = Counter(method_list_attack).values()  #method
count_method_attack_items = Counter(method_list_attack).items()
count_query_attack = Counter(query_list_attack).values()    #query
count_query_attack_items = Counter(query_list_attack).items()
count_status_attack = Counter(status_list_attack).values()  #status
count_status_attack_items = Counter(status_list_attack).items()

#xac suat cua truong thoi gian cho attack log va so sanh gia tri xac suat voi thoi gian tuong ung
for i in count_time_attack:
    ptime_attack.append(float(i)/float(attack_line))
for i in count_time_attack_items:         # fix 14.9
    time_label_attack.append(i[0])
list_ptime = dict(zip(time_list_attack,ptime_attack)) # fix 14.9
for i in time_list_attack:
    for j in range(len(list_ptime.keys())):
        if i == list_ptime.keys()[j]:
            time_compare_attack.append(list_ptime.values()[j])
# pprint (time_compare_attack)
# pprint(time_compare_attack)
#xac suat cua truong method cho attack log va so sanh gia tri xac suat voi thoi gian tuong ug
for i in count_method_attack:
    pmethod_attack.append(float(i)/float(attack_line))
for i in count_method_attack_items:         # fix 14.9
    method_label_attack.append(i[0])
list_pmethod = dict(zip(method_list_attack,pmethod_attack)) # fix 14.9
for i in method_list_attack:
    for j in range(len(list_pmethod.keys())):
        if i == list_pmethod.keys()[j]:
            method_compare_attack.append(list_pmethod.values()[j])
# pprint (method_compare_attack)

for i in count_query_attack:
    pquery_attack.append(float(i)/float(attack_line))
for i in count_query_attack_items:         # fix 14.9
    query_label_attack.append(i[0])
list_pquery = dict(zip(query_label_attack,pquery_attack)) # fix 14.9
for i in query_list_attack:
    for j in range(len(list_pquery.keys())):
        if i == list_pquery.keys()[j]:
            query_compare_attack.append(list_pquery.values()[j])
# pprint(query_compare_attack)

for i in count_status_attack:
    pstatus_attack.append(float(i)/float(attack_line))
for i in count_status_attack_items:         # fix 14.9
    status_label_attack.append(i[0])
list_pstatus_code = dict(zip(status_label_attack,pstatus_attack)) # fix 14.9
for i in status_list_attack:
    for j in range(len(list_pstatus_code.keys())):
        if i == list_pstatus_code.keys()[j]:
            status_compare_attack.append(list_pstatus_code.values()[j])
csv_attackfile.close()

with open('normal_log.csv' , "r+") as csv_normalfile:
    reader_normallog = csv.reader(csv_normalfile)
    for line1 in reader_normallog:
        time_list_normal.append(str(line1[0]))
        method_list_normal.append(str(line1[1]))
        query_list_normal.append(str(line[2]))
        status_list_normal.append(str(line[3]))
count_time_normal = Counter(time_list_normal).values()
count_method_normal = Counter(method_list_normal).values()
count_query_normal = Counter(query_list_normal).values()
count_status_normal = Counter(status_list_normal).values()
for i in count_time_normal:
    #xac xuat cua truong thoi gian cho normal log
    ptime_normal.append(float(i)/float(normal_line))
for i in count_method_normal:
    pmethod_normal.append(float(i)/float(normal_line))
for i in count_query_normal:
    pquery_normal.append(float(i)/float(normal_line))
for i in count_status_normal:
    pstatus_normal.append(float(i)/float(normal_line))
csv_normalfile.close()

