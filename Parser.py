from __future__ import division
from Tkconstants import *
import pandas as pd
import os
import re
import numpy as np


class Backend_Manager():
    def __init__(self, file, path):
        self.data_path = os.path.join(path, file)
        data_path = os.path.join(path, file)
        self.gauge_table = pd.read_csv(data_path)

    def parse(self, item, Text_Fields):
            print('Parsing Item {0}'.format(item))
            cb = CornerBoard_Item(item)
            description = cb.parse()

            Text_Fields['Desc'].delete('1.0',END)
            Text_Fields['Desc'].insert(END, description)
            Text_Fields['Glue'].delete('1.0',END)
            Text_Fields['Glue'].insert(END, "Glue Value")

            legs, gauge, length = cb.get_measurements()
            print(gauge)
            gauge_range = self.lookup_neighbor_indicies(gauge)

            if len(gauge_range) == 1:
                pass
                linear_density = float(self.gauge_table.ix[gauge_range][legs])
                print('Linear Density: ', linear_density)
                Text_Fields['Paper'].delete('1.0', END)
                print('length: ', length)
                PAPER_WEIGHT = str(linear_density * float(length) / 12)
                Text_Fields['Paper'].insert(END, PAPER_WEIGHT)






    def lookup_neighbor_indicies(self, gauge):
        array = self.gauge_table['Thickness ']
        value = gauge
        idx = (np.abs(array-value)).argmin()
        neighbor = array[idx]

        if neighbor > value:
            upper = idx
            lower = idx + 1
            return [upper, lower]

        elif neighbor < value:
            lower = idx
            upper = idx - 1
            return [upper, lower]

        else:
            return [idx]





class CornerBoard_Item():
    def __init__(self, item_code):
        print('Creating CornerBoard Item')
        self.code = item_code
        self.legs = []
        self.gauge = 0
        self.length = 0

        self.gauge_str = ''
        self.legs_str = ''
        self.full_description = ''

    def parse(self):
        cornerboard_item = self.code
        print("\nParsing item %s " % cornerboard_item)
        measurements = cornerboard_item.strip("APCB")

        if (measurements.find("DX") != -1):
            print ("DX Item")
            legs_gauge, self.length = re.split("DX", measurements)
            legs = legs_gauge[0:-3]
            _ , gauge_str = legs_gauge.split(legs)

            self.legs_str = str(legs)
            self.length_str = str(self.length)

            if (len(legs) == 2):
                legsize = [int(legs[0]), int(legs[1])]
                self.legs = list(legsize)


            elif(len(legs) == 4):
                legsize = [int(legs[0:2])/10, int(legs[2:4])/10]
                self.legsize = list(legsize)

            gauge = (int(gauge_str) - 30) / 1000
            self.gauge_str = str(gauge)
            self.gauge = float(gauge)

        elif (measurements.find('-') != -1):
            print('Bundled Item')

        else:
            print ("True Gauge Item")
     #       gauge = measurements[0:-3]

            # 7 -> 2 legs, 3 gauge, 2 length
            # 8 -> 2 legs, 3 gauge, 2 length
            if(len(measurements) == 7 or len(measurements) == 8):
                self.legs_str    = measurements[0:2]
                self.gauge_str = measurements[2:5]
                self.gauge   = int(self.gauge_str)/1000
                legsize = int(self.legs_str[0:int(len(self.legs_str)/2)])
                self.length_str  = measurements[5:]
                self.length = float(self.length_str)
            # 9 -> 4 legs, 3 gauge, 2 length
            # 10-> 4 legs, 3 guage, 3 length
            elif(len(measurements) == 9 or len(measurements) == 10):
                self.legs_str    = measurements[0:4]
                self.gauge_str = measurements[4:7]
                self.gauge   = int(self.gauge_str)/1000
                legsize = int(self.legs_str[0:int(len(self.legs_str)/2)])/10
                self.length_str  = measurements[7:]
                self.length = float(self.length_str)

            # 11, 12-> Fractional Lengths
            elif(len(measurements) == 11):
                pass


            else:
                print('Special Item: Calculate by hand')


        x = len(self.legs_str)
        if(x==2):
            y = 1
        else:
            y = 2



        self.leg1_str = self.legs_str[0:y]
        self.leg2_str = self.legs_str[y:]

        self.full_description = '{0} x {1} \t {2} Ga {3} in '.format(self.leg1_str, self.leg2_str, self.gauge_str , self.length_str)

        return self.full_description


    def get_measurements(self):

        paper_size = sum(self.legs)

        if paper_size == 3:
            leg_dims  = '1.5x1.5'
        elif paper_size == 4:
            leg_dims = '2x2'
        elif paper_size == 5:
            leg_dims = '2.5x2.5'
        elif paper_size == 6:
            leg_dims= '3x3'
        elif paper_size == 8:
            leg_dims = '4x4'
        else:
            print('Error: Invalid Legsize: ', paper_size, self.legs)


        return  leg_dims, float(self.gauge), self.length



def LookupTable():
    def __init__(self):
        pass
