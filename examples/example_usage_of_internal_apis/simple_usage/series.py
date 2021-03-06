"""
series.py
:copyright: (c) 2014-2015 by Onni Software Ltd.
:license: New BSD License, see LICENSE for more details

This shows how to use **SeriesReader** to get the data in various ways
But you can use them with **Reader** class as well
"""
# please install pyexcel-ods
from pyexcel.ext import ods3
from pyexcel import SeriesReader, FilterableReader
from pyexcel.utils import to_dict, to_array
from pyexcel.filters import OddRowFilter, EvenColumnFilter
from pyexcel import Writer
import json

# print all in json
#
# Column 1 Column 2 Column 3
# 1        4        7
# 2        5        8
# 3        6        9
reader = SeriesReader("example_series.ods")
data = to_dict(reader)
print json.dumps(data)
# output:
# {"Column 2": [4.0, 5.0, 6.0], "Column 3": [7.0, 8.0, 9.0], "Column 1": [1.0, 2.0, 3.0]}

# get the column headers
print reader.series()
# [u'Column 1', u'Column 2', u'Column 3']

# get the content in one dimensional array
data = to_array(reader.enumerate())
print data
# [1.0, 4.0, 7.0, 2.0, 5.0, 8.0, 3.0, 6.0, 9.0]

# get the content in one dimensional array
# in reverse order
data = to_array(reader.reverse())
print data

# get the content in one dimensional array
# but iterate it vertically 
data = to_array(reader.vertical())
print data
# [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0]

# get the content in one dimensional array
# but iterate it vertically in revserse
# order
data = to_array(reader.rvertical())
print data
#[9.0, 8.0, 7.0, 6.0, 5.0, 4.0, 3.0, 2.0, 1.0]

# get a two dimensional array
data = to_array(reader.rows())
print data
#[[1.0, 4.0, 7.0], [2.0, 5.0, 8.0], [3.0, 6.0, 9.0]]

# get a two dimensional array in reverse
# order
data = to_array(reader.rrows())
print data
# [[3.0, 6.0, 9.0], [2.0, 5.0, 8.0], [1.0, 4.0, 7.0]]

# get a two dimensional array but stack columns 
data = to_array(reader.columns())
print data
# [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0]]

# get a two dimensional array but stack columns
# in reverse order
data = to_array(reader.rcolumns())
print data
#[[7.0, 8.0, 9.0], [4.0, 5.0, 6.0], [1.0, 2.0, 3.0]]

# filter out odd rows and even columns
reader.filter(OddRowFilter())
reader.filter(EvenColumnFilter())
data = to_dict(reader)
print data
# {u'Column 3': [8.0], u'Column 1': [2.0]}

# and you can write the filtered results
# into a file
w = Writer("example_series_filter.xls")
w.write_reader(reader)
w.close()