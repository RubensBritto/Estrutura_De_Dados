
# -*- coding: utf-8 -*-
import csv

with open('datas/2015.csv') as csv_file:

    csv_reader = csv.DictReader(csv_file, fieldnames=["T", "P", "U"])
    csv_reader.__next__()

    for row in csv_reader:
        print( row["T"] + ', ' + row["P"] + ', ' + row["U"] )
