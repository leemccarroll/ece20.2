# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 03:43:29 2020

@author: Lee
"""

import time
import csv

from envirophat import light, weather, leds
from datetime import datetime

#dt = datetime.now()
csvFile = open('cloud1.csv', 'w')
#csvWrite = year, month, date, hour, lux, temp
leds.off()
#year = dt.year
#month = dt.month
#date = dt.day
#hour = dt.hour
#minute = dt.minute
#second = dt.second

try:
    while True:
        dt= datetime.now()
        year = dt.year
        month = dt.month
        date = dt.day
        hour = dt.hour
        minute = dt.minute
        second = dt.second
        lux = light.light()
        temp = round(weather.temperature(), 1)
        csvWrite = dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second, lux, temp
        writer = csv.writer(csvFile)
        writer.writerow(csvWrite)
        #print('I am here')
        time.sleep(2)

except KeyboardInterrupt:
    leds.off()
    csvFile.close()