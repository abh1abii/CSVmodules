#!/usr/bin/env python3
#The line above is a Shabhang line, telling the OS to use py3 to run this script. 'python3' can be left out from the prefix while running this script.
import csv #CSV operation module
import os #operating system module
import sys #system operation module
import re #regular expression module
filename=sys.argv[1] #input is taken from runtime.
with open(filename) as csv_file, open('out.csv','w') as csv_out: #opens file. Creates out.csv in same folder of script.
    csv_reader = csv.reader(csv_file, delimiter=',')
    writer = csv.writer(csv_out)
    writer.writerow(['CSV File','Iteration', 'Script Path', 'ALF Log', 'Status', 'Cell ID', 'Min', 'Max', 'Avg']) #writes header
    for row in csv_reader:
        ncol=len(row) #stores number of columns
        script_path=row[0]
        alf_log=row[1]
        status=row[2]
        iteration=1
        for i in range(3,ncol):
            if row[i]=="":
                break
            process_string=row[i]
            #print(process_string)
            regex=r"\(PhyCellID: (\d+)\)"
            result=re.search(regex, process_string) #finds match for PhyCellID
            CellID=-1
            if(result!=None): #if match found, updates CellID
                CellID=result[1]
            Min=-1
            regex=r" Min \{\'(\w+)\'\: \'(\d*\.?\d+)" #finds match for Min
            result=re.search(regex, process_string)
            if(result!=None): #if match found, updates Min
                Min=result[2]

            Max=-1
            regex=r" Max \{\'(\w+)\'\: \'(\d*\.?\d+)" #finds match for Max
            result=re.search(regex, process_string)
            if(result!=None): #if match found, updates Max
                Max=result[2]
            Avg=-1
            regex=r" Average \{\'(\w+)\'\: \'(\d*\.?\d+)" #finds match for Average
            result=re.search(regex, process_string)
            if(result!=None): #if match found, updates Average

                Avg=result[2]

            writer.writerow([filename,iteration,script_path,alf_log,status,CellID,Min,Max,Avg]) #writes new row onto out.csv
            iteration=iteration+1
