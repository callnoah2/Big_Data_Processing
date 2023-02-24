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
    filePath = directory + '/area-titles.csv'
fipsDict = {}
with open(filePath, "r") as f:
    for line in f:
        FIPS, areaName = line.strip().split(",", maxsplit=1)
        FIPS = FIPS.strip('""')
        if FIPS[0].isalpha():
            continue
        elif int(FIPS) % 1000 == 0:
            continue
        else:
            fipsDict[FIPS] = areaName


# I need to figure out how to open the annual singlefile.
# then I can split the file into seperate columns for all its data,
# Then I can compare the data to the industry or the software industry
# I am not sure what else I need to do with the data.

num_areas = 0
total_annual_wages_count = 0
max_annual_wage = []
total_estab = 0
max_estab = []
total_empl = 0
max_empl = []
rptdict = {}
for directory2 in sys.argv[1:]:
    path2 = directory2 + '/2021.annual.singlefile.csv'
with open(path2,"r") as file:
    for i in file:
        area_fips, own_code, industry_code, agglvl_code, size_code, year, qtr, disclosure_code, annual_avg_estabs, annual_avg_emplvl, total_annual_wages, taxable_annual_wages, annual_contributions, annual_avg_wkly_wage, avg_annual_pay, lq_disclosure_code, lq_annual_avg_estabs, lq_annual_avg_emplvl, lq_total_annual_wages, lq_taxable_annual_wages, lq_annual_contributions, lq_annual_avg_wkly_wage, lq_avg_annual_pay, oty_disclosure_code, oty_annual_avg_estabs_chg, oty_annual_avg_estabs_pct_chg, oty_annual_avg_emplvl_chg, oty_annual_avg_emplvl_pct_chg, oty_total_annual_wages_chg, oty_total_annual_wages_pct_chg, oty_taxable_annual_wages_chg, oty_taxable_annual_wages_pct_chg, oty_annual_contributions_chg, oty_annual_contributions_pct_chg, oty_annual_avg_wkly_wage_chg, oty_annual_avg_wkly_wage_pct_chg, oty_avg_annual_pay_chg, oty_avg_annual_pay_pct_chg = i.split(",")
        if area_fips.strip('/"') not in fipsDict:
            continue
        if area_fips.strip('/"') == "area_fips":
            continue
        print(industry_code.strip('/"'))
        print(own_code.strip('/"'), " Own code")
        if industry_code.strip('/"') == "10" and own_code.strip('/"') == "0":
            rptdict["all"] = area_fips, own_code, industry_code, total_annual_wages, lq_annual_avg_estabs ,lq_annual_avg_emplvl
        elif industry_code.strip('/"') == 5112 and own_code.strip('/"') == 5:
            rptdict["soft"] = area_fips, own_code, industry_code, total_annual_wages, lq_annual_avg_estabs, lq_annual_avg_emplvl
#         num_areas += 1
#         total_annual_wages_count += int(total_annual_wages.strip('/"'))
#         max_annual_wage.append(total_annual_wages_count)
#         total_estab += float(lq_annual_avg_estabs.strip('/"'))
#         total_empl += float(lq_annual_avg_emplvl.strip('/"'))
# max_annual_wage = max(max_annual_wage)

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
