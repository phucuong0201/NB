import csv
import sys
from pprint import pprint
from collections import Counter

attack_line = 0
normal_line = 0
log_line = []
classify_log_line = []
query_list = []
time_list_attack = []
time_list_normal = []
time_list_classify = []
ptime_attack = []
ptime_normal = []
method_list_attack = []
method_list_normal = []
method_list_classify = []
pmethod_attack = []
pmethod_normal = []
query_list_attack = []
query_list_normal = []
query_list_classify = []
pquery_attack = []
pquery_normal = []
status_list_attack = []
status_list_normal = []
status_list_classify = []
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
    pattacklog = float(attack_line)/float(total_line)
    pnormallog = float(normal_line)/float(total_line)
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

for i in count_time_attack:
    ptime_attack.append(float(i)/float(attack_line))
for i in count_time_attack_items:         # fix 14.9
    time_label_attack.append(i[0])
list_ptime_attack = dict(zip(time_list_attack,ptime_attack)) # fix 14.9
for i in time_list_attack:
    for j in range(len(list_ptime_attack.keys())):
        if i == list_ptime_attack.keys()[j]:
            time_compare_attack.append(list_ptime_attack.values()[j])
for i in count_method_attack:
    pmethod_attack.append(float(i)/float(attack_line))
for i in count_method_attack_items:         
    method_label_attack.append(i[0])
list_pmethod_attack = dict(zip(method_list_attack,pmethod_attack)) 
for i in method_list_attack:
    for j in range(len(list_pmethod_attack.keys())):
        if i == list_pmethod_attack.keys()[j]:
            method_compare_attack.append(list_pmethod_attack.values()[j])
for i in count_query_attack:
    pquery_attack.append(float(i)/float(attack_line))
for i in count_query_attack_items:         
    query_label_attack.append(i[0])
list_pquery_attack = dict(zip(query_list_attack,pquery_attack))
for i in query_list_attack:
    for j in range(len(list_pquery_attack.keys())):
        if i == list_pquery_attack.keys()[j]:
            query_compare_attack.append(list_pquery_attack.values()[j])
for i in count_status_attack:
    pstatus_attack.append(float(i)/float(attack_line))
for i in count_status_attack_items:         
    status_label_attack.append(i[0])
list_pstatus_code_attack = dict(zip(status_label_attack,pstatus_attack)) # fix 14.9
for i in status_list_attack:
    for j in range(len(list_pstatus_code_attack.keys())):
        if i == list_pstatus_code_attack.keys()[j]:
            status_compare_attack.append(list_pstatus_code_attack.values()[j])
csv_attackfile.close()

with open('normal_log.csv' , "r+") as csv_normalfile:
    reader_normallog = csv.reader(csv_normalfile)
    for line in reader_normallog:
        time_list_normal.append(str(line[0]))
        method_list_normal.append(str(line[1]))
        query_list_normal.append(str(line[2]))
        status_list_normal.append(str(line[3]))
count_time_normal = Counter(time_list_normal).values()      #time
count_time_normal_items = Counter(time_list_normal).items()
count_method_normal = Counter(method_list_normal).values()  #method
count_method_normal_items = Counter(method_list_normal).items()
count_query_normal = Counter(query_list_normal).values()    #query
count_query_normal_items = Counter(query_list_normal).items()
count_status_normal = Counter(status_list_normal).values()  #status
count_status_normal_items = Counter(status_list_normal).items()

for i in count_time_normal:
    ptime_normal.append(float(i)/float(normal_line))
for i in count_time_normal_items:         
    time_label_normal.append(i[0])
list_ptime_normal = dict(zip(time_list_normal,ptime_normal)) 
for i in time_list_normal:
    for j in range(len(list_ptime_normal.keys())):
        if i == list_ptime_normal.keys()[j]:
            time_compare_normal.append(list_ptime_normal.values()[j])
for i in count_method_normal:
    pmethod_normal.append(float(i)/float(normal_line))
for i in count_method_normal_items:        
    method_label_normal.append(i[0])
list_pmethod_normal = dict(zip(method_list_normal,pmethod_normal))
for i in method_list_normal:
    for j in range(len(list_pmethod_normal.keys())):
        if i == list_pmethod_normal.keys()[j]:
            method_compare_normal.append(list_pmethod_normal.values()[j])
for i in count_query_normal:
    pquery_normal.append(float(i)/float(normal_line))
for i in count_query_normal_items:         
    query_label_normal.append(i[0])
list_pquery_normal = dict(zip(query_list_normal,pquery_normal))
for i in query_list_normal:
    for j in range(len(list_pquery_normal.keys())):
        if i == list_pquery_normal.keys()[j]:
            query_compare_normal.append(list_pquery_normal.values()[j])
for i in count_status_normal:
    pstatus_normal.append(float(i)/float(normal_line))
for i in count_status_normal_items:        
    status_label_normal.append(i[0])
list_pstatus_code_normal = dict(zip(status_label_normal,pstatus_normal)) 
for i in status_list_normal:
    for j in range(len(list_pstatus_code_normal.keys())):
        if i == list_pstatus_code_normal.keys()[j]:
            status_compare_normal.append(list_pstatus_code_normal.values()[j])
csv_normalfile.close()

time_attack = []
method_attack = []
query_attack = []
status_code_attack = []
pattack = []
plog_in_attack = []
time_normal = []
method_normal = []
query_normal = []
status_code_normal = []
pnormal = []
classify= []
with open('log_to_classify.csv',"r+") as csv_logfile:
    reader_classifylog = csv.reader(csv_logfile)
    for line in reader_classifylog:
        time_list_classify.append(str(line[0]))
        method_list_classify.append(str(line[1]))
        query_list_classify.append(str(line[2]))
        status_list_classify.append(str(line[3]))
        for line in time_list_classify:
            for j in range(len(list_ptime_normal.keys())):
                if line == list_ptime_normal.keys()[j]:
                    time_normal.append(list_ptime_normal.values()[j])
        for line in method_list_classify:
            for j in range(len(list_pmethod_normal.keys())):
                if line == list_pmethod_normal.keys()[j]:
                    method_normal.append(list_pmethod_normal.values()[j])
        for line in query_list_classify:
            for j in range(len(list_pquery_normal.keys())):
                if line == list_pquery_normal.keys()[j]:
                    query_normal.append(list_pquery_normal.values()[j])
        for line in status_list_classify:
            for j in range(len(list_pstatus_code_normal.keys())):
                if line == list_pstatus_code_normal.keys()[j]:
                    status_code_normal.append(list_pstatus_code_normal.values()[j])
        group_pnormal = zip(time_normal, method_normal, query_normal, status_code_normal)
        for i in group_pnormal:
            pnormal.append(i[0]*i[1]*i[2]*i[3]*pnormallog)
        for line in time_list_classify:
            for j in range(len(list_ptime_attack.keys())):
                if line == list_ptime_attack.keys()[j]:
                    time_attack.append(list_ptime_attack.values()[j])
        for line in method_list_classify:
            for j in range(len(list_pmethod_attack.keys())):
                if line == list_pmethod_attack.keys()[j]:
                    method_attack.append(list_pmethod_attack.values()[j])
        for line in query_list_classify:
            for j in range(len(list_pquery_attack.keys())):
                if line == list_pquery_attack.keys()[j]:
                    query_attack.append(list_pquery_attack.values()[j])
        for line in status_list_classify:
            for j in range(len(list_pstatus_code_attack.keys())):
                if line == list_pstatus_code_attack.keys()[j]:
                    status_code_attack.append(list_pstatus_code_attack.values()[j])
        group_pattack = zip(time_attack, method_attack, query_attack, status_code_attack)
        for i in group_pattack:
            pattack.append(i[0]*i[1]*i[2]*i[3]*pattacklog)
        group_plog = zip(pnormal, pattack)
    for i in group_plog:
        if i[0] > i[1]:
            classify.append('An toan')
        if i[0] < i[1]:
            classify.append('Bi tan cong')

    with open('log.txt', 'r+') as f:
        lines = []
        for line in f:
            lines.append(line)
        group_log_classify = zip(lines, classify)
        pprint(group_log_classify)

