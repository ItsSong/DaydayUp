#!/usr/bin/env python
#-*- coding = utf-8 -*-
dayup = 1.0
dayfactor = 0.01
sum = 0
for i in range(365):
    if i%7 in [6,0]:
        dayup = dayup*(1-dayfactor)
    else:
        dayup = dayup*(1+dayfactor)
print("工作日的力量是{:.2f}".format(dayup))
