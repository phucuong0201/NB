import csv
import sys

filename = open ('log.csv' ,"r+")
reader = csv.reader(filename)

#Xac suat xuat hien cua hai gia thuyet
attack_line = 0
normal_line = 0
count_time = 0
for line in reader:
    time = line[0]
    method = line[1]
    request = line[2]
    status = line[3]
    label = line[4]
    label_list = list(label)
    method_list = list(method)
    for x  in label:
        if x == '1':
            attack_line += 1
        if x == '0':
            normal_line += 1
# total_line = attack_line + normal_line
# Pattack = float(attack_line) / float(total_line)
# Pc1 = float(1/x)
# Pnormal = float(normal_line) / float(total_line)
    get_in_attack = 0    
    for x in label:
        if x == '1':
            for y in method:
                if y == '0':
                    get_in_attack +=1
                print get_in_attack
# Pc2 = float(1/y)
# print time_list
# print total_line
# print Pattack
# print Pnormal


#Tinh toan xac suat cua method
# filename = open ('log.csv' ,"r+")
# reader = csv.reader(filename)
# for line in reader:
#     method = line[1]
#     label = line[4]
#     label_list = list(label)
#     method_list = list(method)
#     get_in_attack = 0
#     post_in_attack = 0
#     head_in_attack = 0
#     delete_in_attack = 0
#     put_in_attack = 0
#     options_in_attack = 0
#     trace_in_attack = 0
#     connect_in_attack = 0
#     # print method_list
#     for x in label:
#         if x == '1':
#             if method == '0':
#                 get_in_attack +=1
#             # print get_in_attack
#             if method == '1':
#                 post_in_attack +=1
#             # print post_in_attack
#             if method == '2':
#                 head_in_attack +=1
#             # print head_in_attack
#             if method == '3':
#                 delete_in_method +=1
#                 print delete_in_method


