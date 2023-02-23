#!/usr/bin/env python  	  	  

#                         ,  	  	  
#                        (o)<  DuckieCorp Software License  	  	  
#                   .____//  	  	  
#                    \ <' )   Copyright (c) 2023 Erik Falor  	  	  
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  	  	  
#         TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION  	  	  
#  	  	  
# You may reproduce and distribute copies of the Work in any medium,  	  	  
# with or without modifications, provided that You meet the following  	  	  
# conditions:  	  	  
#  	  	  
#   (a) You must give any other recipients of the Work a copy of this  	  	  
#       License; and  	  	  
#   (b) You must cause any modified files to carry prominent notices  	  	  
#       stating that You changed the files; and  	  	  
#   (c) You must retain, in the Source form of the files that You  	  	  
#       distribute, all copyright, patent, trademark, and attribution  	  	  
#       notices from the Source form of the Work; and  	  	  
#   (d) You do not misuse the trade names, trademarks, service marks,  	  	  
#       or product names of the Licensor, except as required for  	  	  
#       reasonable and customary use of the source files.  	  	  

import time  	  	  
import sys  	  	  
from report import print_report

# print_report takes a dictionary with these contents:  	  	  
rpt = {  	  	  
        'year': 2021,  	  	  

        'all': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  

        'soft': {  	  	  
            'num_areas': 0,  	  	  
            'total_annual_wages': 0,  	  	  
            'max_annual_wage': ["", 0],  	  	  
            'total_estab': 0,  	  	  
            'max_estab': ["", 0],  	  	  
            'total_empl': 0,  	  	  
            'max_empl': ["", 0],  	  	  
        },  	  	  
}  	  	  

if len(sys.argv) <= 1:
    print("Too few arguments")
    exit()

print("Reading the databases...", file=sys.stderr)  	  	  
before = time.time()  	  	  

for directory in sys.argv[1:]:
    file_path = directory + '/area-titles.csv'

with open(file_path, "r") as f:
    for line in f:
        FIPS, areaName = line.strip().split(",", maxsplit=1)
        FIPS = FIPS.strip('""')
        if FIPS[0].isalpha():
            continue
        elif int(FIPS) % 1000 == 0:
            continue
        else:
            print(FIPS)

print("TODO: if opening the file 'sys.argv[1]/area-titles.csv' fails, let your program crash here")  # DELETE ME
print("TODO: Convert the file 'sys.argv[1]/area-titles.csv' into a dictionary")  # DELETE ME  	  	  
print("TODO: the FIPS dictionary should contain 3,463 pairs")  # DELETE ME
# I need to figure out how to open the annual singlefile.
# then I can split the file into seperate columns for all its data,
# Then I can compare the data to the industry or the software industry
# I am not sure what else I need to do with the data.


# for directory2 in sys.argv[1:]:
#     path2 = directory2 + '/2021.annual.singlefile.csv'
# with open(path2,"r") as file:
#     for i in file:
#         print(i)
print("TODO: if opening the file 'sys.argv[1]/2021.annual.singlefile.csv' fails, let your program crash here")  # DELETE ME  	  	  
print("TODO: Collect information from 'sys.argv[1]/2021.annual.singlefile.csv'")  # DELETE ME  	  	  

print("TODO: Fill in the report dictionary for all industries")  # DELETE ME  	  	  
rpt['all']['num_areas']           = 1337  	  	  

rpt['all']['total_annual_wages']  = 13333337  	  	  
rpt['all']['max_annual_wage']     = ["Trantor", 123456]  	  	  

rpt['all']['total_estab']         = 42  	  	  
rpt['all']['max_estab']           = ["Terminus", 12]  	  	  

rpt['all']['total_empl']          = 987654  	  	  
rpt['all']['max_empl']            = ["Anacreon", 654]  	  	  


print("TODO: Fill in the report dictionary for the software publishing industry")  # DELETE ME  	  	  
rpt['soft']['num_areas']          = 1010  	  	  

rpt['soft']['total_annual_wages'] = 101001110111  	  	  
rpt['soft']['max_annual_wage']    = ["Helicon", 110010001]  	  	  

rpt['soft']['total_estab']        = 1110111  	  	  
rpt['soft']['max_estab']          = ["Solaria", 11000]  	  	  

rpt['soft']['total_empl']         = 100010011  	  	  
rpt['soft']['max_empl']           = ["Gaia", 10110010]  	  	  


after = time.time()  	  	  
print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)  	  	  


# Print the completed report  	  	  
print_report(rpt)  	  	  

print("\n\nTODO: did you delete all of the TODO messages?")  # DELETE ME  	  	  
