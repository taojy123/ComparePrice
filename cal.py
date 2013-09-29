# -*- coding: cp936 -*-
import btcchina
import bitstamp
import re

s_str = bitstamp.get_data()
c_str = btcchina.get_data()

s_data = eval(s_str)
s_data = s_data["bids"][:25]

c_str = c_str[c_str.find("bid")-80*30:c_str.find("bid")]
regex = re.compile(r'{"price":"(.*?)","totalamount":"(.*?)","type":"ask"}')
c_data = regex.findall(c_str)
c_data = c_data[-25:]

print s_data
print c_data


RATE = 6.1086

gap = None
s_sum = 0
c_sum = 0
for i in range(5):
    s_price = float(s_data[i+4][0])
    c_price = float(c_data[i+4][0])
    s_totalamount = sum([float(s_data[i][1]),
                      float(s_data[i+1][1]),
                      float(s_data[i+2][1]),
                      float(s_data[i+3][1]),
                      float(s_data[i+4][1])])
    c_totalamount = sum([float(c_data[i][1]),
                      float(c_data[i+1][1]),
                      float(c_data[i+2][1]),
                      float(c_data[i+3][1]),
                      float(c_data[i+4][1])])
    s_sum += s_totalamount
    c_sum += c_totalamount
    print s_price,"|",s_totalamount,"    ",c_price,"|",c_totalamount
    if gap is None:
        gap = s_price * 0.995 * RATE - c_price
        gap_percent = gap / c_price * 100
        SUM = min(s_totalamount, c_totalamount)
print "价差%:", gap_percent
print "SUM:", SUM






    
