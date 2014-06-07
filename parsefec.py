# FEC data processor
# Copyright (C) 2013-2014 James Michael DuPont
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import csv
#fec_reader = csv.reader(open('data.csv'))
#or
fec_dict_reader = csv.DictReader(open('data.csv'), delimiter=',', quotechar='"')
from collections import defaultdict
matrix = defaultdict(dict)

for line in fec_dict_reader:
    amnt = int(line["TransactionAmount"])

    if (amnt <  0) :
        print amnt, line

    if not (    line['RecipientState'] in   matrix         and         line['DonorState'] in matrix [  line['RecipientState']   ]    ) :
        matrix [ line['RecipientState']    ][  line['DonorState'] ] = 0
        
    matrix [  line['RecipientState']    ][ line['DonorState'] ] += amnt



for receipt in sorted(matrix.keys()):
    print receipt
    for send in sorted(matrix[receipt].keys()):
        v = matrix [receipt][send ] 
        print receipt, send,v
