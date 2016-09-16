  
import csv
import sys
from pprint import pprint
from collections import Counter

# filename = open ('log.csv' , "r+")

											# reader = csv.reader(filename)
											# attack_line = 0
											# normal_line = 0
											# list_label  = []
											# list_time = []
											# count_time = 0
											# for line in reader:
											#     list_label.append(str(line[4]))
											#     list_time.append(str(line[0]))
											# for x in range(len(list_label)):
											#     if list_label[x] == '1':
											#         attack_line += 1
											#     if list_label[x] == '0':
											#         normal_line += 1
											# total_line = attack_line + normal_line
											# Pattack = float(attack_line)/float(total_line)
											# Pnormal = float(normal_line)/float(total_line)


											# pprint (Counter(list_time).items())
attack_log_file = open("attack_log.csv", "r")
normal_log_file = open("normal_log.csv", "r")
list_method = []
get_in_attack = 0
with open ("attack_log.csv","r") as attacklog:
	attack_log_reader = csv.reader(attacklog,delimiter = ",")
	attack_log_line = list(attack_log_reader)
	attack_log_row_count = len(attack_log_line)
	get_in_attack = 0
	post_in_attack = 0
	head_in_attack = 0
	delete_in_attack = 0
	put_in_attack = 0
	options_in_attack = 0
	trace_in_attack = 0
	connect_in_attack = 0
	list_method  = []
	for line in attack_log_line:
	    list_method.append(str(line[1]))
	for x in range(len(list_method)):
	    if list_method[x] == '0':
	        get_in_attack += 1
	    if list_method[x] == '1':
	    	post_in_attack += 1
	    if list_method[x] == '2':
	    	head_in_attack += 1
	    if list_method[x] == '3':
	    	delete_in_attack += 1
	    if list_method[x] == '4':
	    	put_in_attack += 1
	    if list_method[x] == '5':
	    	options_in_attack += 1
	    if list_method[x] == '6':
	    	trace_in_attack += 1
	    if list_method[x] == '7':
	    	connect_in_attack += 1
	        
# print list_method
# print get_in_attack
# print post_in_attack
with open ("normal_log.csv", "r") as normallog:
	normal_log_reader = csv.reader(normallog, delimiter = ",")
	normal_log_line = list(normal_log_reader)
	normal_log_row_count = len(normal_log_line)
	get_in_normal = 0
	post_in_normal = 0
	head_in_normal = 0
	delete_in_normal = 0
	put_in_normal = 0
	options_in_normal = 0
	trace_in_normal = 0
	connect_in_normal = 0
	status_code_200_in_normal = 0
	list_method  = []
	list_status_code_normal = []
	for line in normal_log_line:
	    list_method.append(str(line[1]))
	for x in range(len(list_method)):
	    if list_method[x] == '0':
	        get_in_normal += 1
	    if list_method[x] == '1':
	    	post_in_normal += 1
	    if list_method[x] == '2':
	    	head_in_normal += 1
	    if list_method[x] == '3':
	    	delete_in_normal += 1
	    if list_method[x] == '4':
	    	put_in_normal += 1
	    if list_method[x] == '5':
	    	options_in_normal += 1
	    if list_method[x] == '6':
	    	trace_in_normal += 1
	    if list_method[x] == '7':
	    	connect_in_normal += 1
# 	for line in normal_log_line:
# 		list_status_code_normal.append(str(line[2]))
# 	for x in range(len(list_status_code_normal)):
# 		count = Counter(list_status_code_normal)
# print count 

total_line = normal_log_row_count + attack_log_row_count

Pattack = float(attack_log_row_count) / float(total_line)
Pnormal = float(normal_log_row_count) / float(total_line)

#tinh xac suat xuat hien cua cac method ben trong dong log tan cong
Pget_in_attack = float(get_in_attack) / float(total_line)
Ppost_in_attack = float(post_in_attack) / float(total_line)
Phead_in_attack = float(head_in_attack) / float(total_line)
Pdelete_in_attack = float(delete_in_attack) / float(total_line)
Pput_in_attack = float(put_in_attack) / float(total_line)
Poptions_in_attack = float(options_in_attack) / float(total_line)
Ptrace_in_attack = float(trace_in_attack) / float(total_line)
Pconnect_in_attack = float(connect_in_attack) / float(total_line)
#

#Tinh xac suat xuat hien cua method trong dong log binh thuong
Pget_in_normal = float(get_in_normal) / float(total_line)
Ppost_in_normal = float(post_in_normal) / float(total_line)
Phead_in_normal = float(head_in_normal) / float(total_line)
Pdelete_in_normal = float(delete_in_normal) / float(total_line)
Pput_in_normal = float(put_in_normal) / float(total_line)
Poptions_in_normal = float(options_in_normal) / float(total_line)
Ptrace_in_normal = float(trace_in_normal) / float(total_line)
Pconnect_in_normal = float(connect_in_normal) / float(total_line)
#
print ("Xac suat get trong attack la: ", Pget_in_attack)
print ("Xac suat post trong attack la: ", Ppost_in_attack)
print ("Xac suat get trong normal la: ", Pget_in_normal)
print ("Xac suat post trong normal la", Ppost_in_normal)
# pprint (Counter(list_method).values())
# pprint (Counter(list_status_code_normal))
