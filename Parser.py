from __future__ import division
from Tkconstants import *
import pandas as pd
import os
import re
import numpy as np
from Tkinter import Tk



class Backend_Manager():
    def __init__(self, parent,  paper_table, liner_table, path):
        self.parent = parent
        paper_path = os.path.join(path, paper_table)
        liner_table = os.path.join(path, liner_table)
        self.liner_table = pd.read_csv(liner_table)
        self.lookup_table = pd.read_csv(paper_path)
        self.Text_Fields = dict()
        self.whse = 1   # Set to 001 by default

    def parse(self, item):
            print('Parsing Item {0}'.format(item))
            try:
                cb = CornerBoard_Item(item)
                self.parent.clipboard_clear()
                self.parent.clipboard_append(item)
                cb.whse = self.whse
                description = cb.parse()
                PAPER_WEIGHT = cb.get_paper_weight(self.lookup_table)
                LINER_WEIGHT = cb.get_liner_weight(self.liner_table)
                GLUE_WEIGHT = cb.get_glue_weight()
                self.update_txt('Desc', description)
                self.update_txt('Glue', GLUE_WEIGHT)
                self.update_txt('Paper', PAPER_WEIGHT)
                self.update_txt('Liner',  LINER_WEIGHT)
            except:
                self.update_txt('Desc', 'Invalid Item')
                self.update_txt('Glue', '')
                self.update_txt('Paper', '')
                self.update_txt('Liner', '')

    def update_txt(self, field, text):
        self.Text_Fields[field].delete('1.0',END)
        self.Text_Fields[field].insert(END, text)

    def set_text_dict(self, text_fields):
        self.Text_Fields = text_fields

    def switch_warehouse(self, whse):
        if (whse == 1):
            self.whse = 1

        else:
            self.whse = 1.15



class CornerBoard_Item():
    def __init__(self, item_code):
        print('Creating CornerBoard Item')
        self.code = item_code
        self.legs = []
        self.gauge = 0
        self.length = 0
        self.total_legs_size = 0
        self.standard_legs_str = ''
        self.gauge_str = ''
        self.legs_str = ''
        self.full_description = ''

    def parse(self):
        cornerboard_item = self.code
        print("\nParsing item %s " % cornerboard_item)
        measurements = cornerboard_item.strip("APCB")


        if (measurements.find("DX") != -1):
            print ("DX Item")
            legs_gauge, self.length_str = re.split("DX", measurements)
            self.legs_str = legs_gauge[0:-3]
            _ , self.gauge_str = legs_gauge.split(self.legs_str)
            self.length = float(self.length_str)

            if (len(self.legs_str) == 2):
                legsize = [int(self.legs_str[0]), int(self.legs_str[1])]
                self.legs = list(legsize)

            elif(len(self.legs_str) == 4):
                leg1 = self.legs_str[0:2]
                leg2 = self.legs_str[2:4]
                legsize = [int(leg1)/10, int(leg2)/10]
                self.legs = list(legsize)

            gauge = (int(self.gauge_str) - 30) / 1000
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
                legsize = [int(self.legs_str[0]),int(self.legs_str[1])]
                self.legs = list(legsize)
                self.length_str  = measurements[5:]
                self.length = float(self.length_str)
            # 9 -> 4 legs, 3 gauge, 2 length
            # 10-> 4 legs, 3 guage, 3 length
            elif(len(measurements) == 9 or len(measurements) == 10):
                self.legs_str    = measurements[0:4]
                self.gauge_str = measurements[4:7]
                self.gauge   = int(self.gauge_str)/1000
                leg1 = self.legs_str[0:2]
                leg2 = self.legs_str[2:4]
                legsize = [int(leg1)/10, int(leg2)/10]
                self.legs = list(legsize)
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


    def get_standard_legs_str(self):
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
            return 'Null'

        return  leg_dims

    def lookup_neighbor_indicies(self, table):
        array = table['Thickness ']
        value = self.gauge
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

    def calc_linear_paper_density(self, table ):
        self.standard_legs = self.get_standard_legs_str()
        gauge_range = self.lookup_neighbor_indicies(table)
        table_value = float(table.ix[gauge_range][self.standard_legs])
        return table_value

    def get_paper_weight(self,table):
        linear_density = self.calc_linear_paper_density(table)
        length_feet = self.length / 12
        paper_weight   = linear_density * length_feet * self.whse
        return '{0:.3f}'.format(paper_weight)



    def get_liner_weight(self, liner_table):
        print(liner_table)
        liner_density = float(liner_table[self.standard_legs] / 12)
        liner_weight = liner_density * self.length
        return '{0:.3f}'.format(liner_weight)


    def get_glue_weight(self):
        #Glue Model is linear in length and leg size
        #Quadratic in Gauge
        glue_weight = sum(self.legs) * self.length * .00029
        return '{0:.3f}'.format(glue_weight)
