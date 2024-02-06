#!/usr/bin/env python


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

# Create a dictionary mapping FIPS codes to area names
fipsDict = {}
count = 0
for directory in sys.argv[1:]:
    filePath = directory + '/area-titles.csv'
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
                count += 1

# Read the annual singlefile and add data to the report
for directory2 in sys.argv[1:]:
    path2 = directory2 + '/2021.annual.singlefile.csv'
    with open(path2, "r") as file:
        for line in file:
            if line[1].strip('/"') == "a":
                continue
            # Split the CSV line into separate fields
            fields = line.strip().split(",")
            area_fips = fields[0].strip('/"')
            own_code = fields[1].strip('/"')
            industry_code = fields[2].strip('/"')
            total_annual_wages = int(fields[10].strip('/"'))
            lq_annual_avg_estabs = float(fields[17].strip('/"'))
            lq_annual_avg_emplvl = float(fields[18].strip('/"'))
            # Skip this line if the FIPS code is not in our dictionary
            if area_fips not in fipsDict:
                continue

            # Add data to the report
            if industry_code == "10" and own_code == "0":
                rpt['all']['num_areas'] += 1
                rpt['all']['total_annual_wages'] += total_annual_wages
                if total_annual_wages > rpt['all']['max_annual_wage'][1]:
                    rpt['all']['max_annual_wage'] = [fipsDict[area_fips], total_annual_wages]
                rpt['all']['total_estab'] += lq_annual_avg_estabs
                if lq_annual_avg_estabs > rpt['all']['max_estab'][1]:
                    rpt['all']['max_estab'] = [fipsDict[area_fips], lq_annual_avg_estabs]
                rpt['all']['total_empl'] += lq_annual_avg_emplvl
                if lq_annual_avg_emplvl > rpt['all']['max_empl'][1]:
                    rpt['all']['max_empl'] = [fipsDict[area_fips], lq_annual_avg_emplvl]

            if industry_code == "5112" and own_code == "5":
                rpt['soft']['num_areas'] += 1
                rpt['soft']['total_annual_wages'] += total_annual_wages
                if total_annual_wages > rpt['soft']['max_annual_wage'][1]:
                    rpt['soft']['max_annual_wage'] = [fipsDict[area_fips], total_annual_wages]
                rpt['soft']['total_estab'] += lq_annual_avg_estabs
                if lq_annual_avg_estabs > rpt['soft']['max_estab'][1]:
                    rpt['soft']['max_estab'] = [fipsDict[area_fips], lq_annual_avg_estabs]
                rpt['soft']['total_empl'] += lq_annual_avg_emplvl
                if lq_annual_avg_emplvl > rpt['soft']['max_empl'][1]:
                    rpt['soft']['max_empl'] = [fipsDict[area_fips], lq_annual_avg_emplvl]
print_report(rpt)
